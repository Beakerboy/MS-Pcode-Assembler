import struct


class ModuleCache():

    def __init__(self, version, project_cookie, syskind=2):
        self.version = version
        self.syskind = syskind
        self.project_cookie = project_cookie
        self.rfff_value = b'\x00' * 5
        self.clear_variables()

    def get_vba_version(self):
        if self.version >= 0x6B:
            if self.version >= 0x97:
                return 7
            else:
                return 6
        else:
            return 5

    def is_64bit(self):
        return self.syskind == 3

    def clear_variables(self):
        self.module_cookie = 0
        self.misc = []
        # utf-16 encoded guid with opening "0{" and closing bracket.
        self.guid = b''
        self.guids1 = b'\x00' * 48
        self.guids_extra = []
        self.guids2 = b'\x00' * 32
        self.declaration_table = b''
        self.indirect_table = b''
        self.object_table = b''
        self.df_data = []
        self.pcode = b''
        self.rfff_data = []

    def to_bytes(self) -> bytes:
        ca = self.header_section()
        ca += self.declaration_table_section()
        ca += guid_section()
        ca += struct.pack("<hIIihIhIhHIHhIH", 0x454D, -1, -1, 0, -1,
                          0, -1, 0x0101, 0, 0xDF, -1, 0, self.misc[5])
        ca += b'\xFF' * 0x80
        ca += struct.pack("<I", len(self.object_table)) + self.object_table
        ca += struct.pack("<hHI", -1, 0x0101, 0)
        if len(self.guid) > 0:
            ca += struct.pack("<HH", 1, len(self.guid)) + self.guid
        else:
            ca += struct.pack("<H", 0)
        ca += struct.pack("<IHiH", 0, 0, -1, 0x0101)
        ca += struct.pack("<I", len(self.indirect_table)) + self.indirect_table
        ca += struct.pack("<HhHH", 0, -1, 0, self.misc[7])
        fo = ("00 00 00 00 00 00 00 00"
              "FF FF FF FF FF FF FF FF FF FF FF FF", self.misc[6],
              "FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
              "FF FF FF FF", self.misc[6], "FF FF FF FF FF FF FF FF",
              "FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00",
              "00 00 00 00 FF FF 00 00 FF FF FF FF FF FF 00 00",
              "00 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
              "FF FF FF FF FF FF FF FF FF FF 00 00 FF FF FF FF",
              "FF FF")
        ca += bytes.fromhex(" ".join(fo))
        ca += self.rff_section()
        ca += self.df_section()
        ca += b'\x00' * 58
        ca += self._create_pcode()
        return ca

    def header_section(self) -> bytes:
        oto = self.object_table_offset() - 0x8A
        ito = self.id_table_offset() - 10
        magic_ofs = self.magic_offset() - 0x3C
        myo = self.mystery_offset()
        return struct.pack("<BIIIIIiIIIIHHHhIIHhH", 1, self.misc[0],
                           oto, myo, 0xD4, ito, -1, magic_ofs,
                           self.misc[1], 0, 1, self.project_cookie,
                           self.module_cookie, 0, -1, self.misc[2],
                           self.misc[3], 0xB6, -1, 0x0101)

    def declaration_table_section(self) -> bytes:
        ca = len(self.declaration_table).to_bytes(4, "little")
        ca += self.declaration_table
        return ca + struct.pack("<iI", -1, 0)

    def guid_section(self) -> bytes:
        ca = struct.pack("<hhhH", -1, -1, -1, 0)
        ca += self.guids1
        ca += len(self.guids_extra).to_bytes(4, "little")
        ca += struct.pack("<IIIIiiHIiIB", 0x10, 3, 5, 7, -1, -1, 0x0101,
                          8, -1, 0x78, self.misc[4])
        ca += self.guids2
        ca += struct.pack("<hI", -1, 0)
        return ca

    def rff_section(self) -> bytes:
        rfff_string = b''
        for rfff in self.rfff_data:
            str16 = bytes(rfff, "utf_16_le")
            size = len(str16).to_bytes(2, "little")
            rfff_string += size + str16
        return self.rfff_value + b'\x00' + rfff_string + b'\xDF'

    def df_section(self) -> bytes:
        df_count = len(self.df_data)
        df_string = b''
        if df_count > 0:
            df_string = (0).to_bytes(4, "little")
            for df in self.df_data:
                df_string += struct.pack("<iIHH", df[0], df[1], df[2], df[3])
        return df_count .to_bytes(2, "little") + df_string

    def object_table_offset(self) -> int:
        """
        The object table offset is 8A less than the position.
        The object table is between the block of F's and the
        Utf-16 Guid.
        """
        return 0x017A + len(self.guids_extra) * 16

    def id_table_offset(self) -> int:
        guid_len = 2 if len(self.guid) == 0 else 0x52
        ob_len = len(self.object_table) + 4
        return self.object_table_offset() + ob_len + guid_len + 0x12

    def magic_offset(self):
        in_len = len(self.indirect_table) + 4
        return self.id_table_offset() + 0xC7 + in_len

    def mystery_offset(self):
        return self.magic_offset() - 0x43

    def _create_pcode(self) -> bytes:
        num = 0
        pcode = struct.pack("<HHH", 0xCAFE, 1, num)
        for i in range(num):
            pass
        pcode += struct.pack("<iHI", -1, 0x0101, 8)
        # Pcode Table
        # Footer?
        pcode += struct.pack("<iIiH", -1, 0x78, -1, 0)
        return pcode

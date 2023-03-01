import struct


class ModuleCache():

    def __init__(self, version, syskind, project_cookie):
        self.version = version
        self.syskind = 2
        self.project_cookie = project_cookie
        self.clear_variables()

    def get_vba_version(self):
        if self.version >= 0x6B:
            if version >= 0x97:
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
        self.guids1 = b'\xff' * 4 + b'\x00' * 54
        self.guids2 = b'\x00' * 32
        self.indirect_table = b''
        self.object_table = b''
        self.df_data = []
        self.pcode = b''

    def to_bytes(self) -> bytes:
        oto = self.object_table_offset() - 0x8A
        ito = self.id_table_offset() - 10
        magic_ofs = self.magic_offset() - 0x3C
        myo = self.mystery_offset()
        ca = struct.pack("<BIIIIIiIIIIHHHhIIHhHIiIh", 1, self.misc[0],
                         oto, myo, 0xD4, ito, -1, magic_ofs,
                         self.misc[1], 0, 1, self.project_cookie,
                         self.module_cookie, 0, -1, self.misc[2],
                         self.misc[3], 0xB6, -1, 0x0101, 0, -1, 0, -1)
        ca += self.guids1
        ca += struct.pack("<IIIIiiHIiIB", 0x10, 3, 5, 7, -1, -1, 0x0101,
                          8, -1, 0x78, self.misc[4])
        ca += self.guids2
        ca += struct.pack("<hIIihIhIhHIHhIH", -1, 0, 0x454D, -1, -1, 0, -1,
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
              "FF FF 00 00 00 00 00 00 ")
        df_count = len(self.df_data).to_bytes(2, "little")
        if df_count > 0:
            df_string = 0.to_bytes(4, "little")
            for df in self.df_data:
                df_string += struct.pack("<iIHH", df[0], df[1], df[2[, df[3])
        fo += b'\xDF' + df_count + df_string + b'\x00' * 58
        ca += bytes.fromhex(" ".join(fo))
        ca += self._create_pcode()
        return ca

    def object_table_offset(self) -> int:
        """
        The object table offset is 8A less than the position.
        The object table is between the block of F's and the
        Utf-16 Guid.
        """
        return 0x0140 + len(self.guids1)

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

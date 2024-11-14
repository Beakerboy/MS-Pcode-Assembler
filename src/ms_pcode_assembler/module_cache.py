import struct
import ms_pcode_assembler as mspc
from typing import TypeVar
from uuid import UUID


T = TypeVar('T', bound='ModuleCache')


class ModuleCache():

    import mspc.cache_header as ch
    from ch import CacheHeader
    def __init__(self: T, version: int, project_cookie: int,
                 syskind: int = 2, signature: int = 0) -> None:
        self.version = version
        self.header = ch.CacheHeader(self, project_cookie, syskind, signature)
        self.rfff_value = b'\x00' * 5
        self.zeroes = 58
        self.clear_self()

    def get_vba_version(self: T) -> int:
        '''
        Where is this used?
        '''
        if self.version >= 0x6B:
            if self.version >= 0x97:
                return 7
            else:
                return 6
        else:
            return 5

    def is_64bit(self: T) -> bool:
        return self.syskind == 3

    def clear_variables(self: T) -> None:
        self.header.clear_variables()
        self.clear_self()

    def clear_self(self: T) -> None:
        self.module_cookie = 0
        self.misc = []
        zero_guid = UUID(int=0x0)
        # utf-16 encoded guid with opening "0{" and closing bracket.
        self.guid = []
        self.guids1 = [zero_guid, zero_guid, zero_guid]
        self.guids_extra = []
        self.guids2 = [zero_guid, zero_guid]
        self.declaration_table = b''
        self.indirect_table = b''
        self.object_table = b''
        self.df_data = []
        self.pcode = struct.pack("<iI", -1, 0x78)
        self.pcode_dir = b''
        self.rfff_data = []
        self.f_data = b''

    def to_bytes(self: T) -> bytes:
        ca = b'\x01'
        ca += self.header.to_bytes()
        ca += self.declaration_table_section()
        ca += self.guid_section()
        ca += self.four_five_section()
        ca += self.object_table_section()
        ca += self.utf16_guid_section()
        ca += self.indirect_table_section()
        ca += self.f_section()
        ca += self.rff_section()
        ca += self.df_section()
        ca += b'\x00' * self.zeroes
        ca += self._create_pcode()
        return ca

    def declaration_table_section(self: T) -> bytes:
        ca = len(self.declaration_table).to_bytes(4, "little")
        ca += self.declaration_table
        return ca + struct.pack("<iI", -1, 0)

    def guid_section(self: T) -> bytes:
        misc = self.misc[0]
        ca = struct.pack("<hhhH", -1, misc[0], -1, 0)
        for guid in self.guids1:
            ca += guid.bytes_le
        ca += len(self.guids_extra).to_bytes(4, "little")
        for guid in self.guids_extra:
            ca += guid.bytes_le
        ca += struct.pack("<IIIIiiHIiIB", 0x10, 3, 5, 7, -1, -1, 0x0101,
                          8, -1, 0x78, misc[1])
        for guid in self.guids2:
            ca += guid.bytes_le
        ca += struct.pack("<hI", -1, 0)
        return ca

    def four_five_section(self: T) -> bytes:
        misc = self.misc[1]
        return (struct.pack("<IihIhIhHIHhIH", 0x454D, -1, -1, 0, -1,
                            0, -1, 0x0101, 0, 0xDF, -1, 0, misc)
                + b'\xFF' * 0x80)

    def object_table_section(self: T) -> bytes:
        ca = struct.pack("<I", len(self.object_table)) + self.object_table
        ca += struct.pack("<hHI", -1, 0x0101, 0)
        return ca

    def utf16_guid_section(self: T) -> bytes:
        misc = self.misc[2]
        ca = len(self.guid).to_bytes(2, "little")
        if len(self.guid) > 0:
            guid_str = "0"
            for guid in self.guid:
                guid_str += "{" + str(guid).upper() + "}"
            guid_str_bytes = bytes(guid_str, "utf_16_le")
            ca += len(guid_str_bytes).to_bytes(2, "little") + guid_str_bytes
        ca += struct.pack("<IHiH", misc, 0, -1, 0x0101)
        return ca

    def indirect_table_section(self: T) -> bytes:
        return (struct.pack("<I", len(self.indirect_table))
                + self.indirect_table)

    def f_section(self: T) -> bytes:
        misc = self.misc[3]
        if self.f_data == b'':
            ca = struct.pack("<HhHH", 0, -1, 0, misc[0])
            fo = ("00 00 00 00 00 00 00 00"
                  "FF FF FF FF FF FF FF FF FF FF FF FF", misc[1],
                  "FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
                  "FF FF FF FF", misc[1], "FF FF FF FF FF FF FF FF",
                  "FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00",
                  "00 00 00 00 FF FF 00 00 FF FF FF FF FF FF 00 00",
                  "00 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
                  "FF FF FF FF FF FF FF FF FF FF 00 00 FF FF FF FF",
                  "FF FF")
            ca += bytes.fromhex(" ".join(fo))
        else:
            ca = self.f_data
        return ca

    def rff_section(self: T) -> bytes:
        rfff_string = b''
        for rfff in self.rfff_data:
            str16 = bytes(rfff, "utf_16_le")
            size = len(str16).to_bytes(2, "little")
            rfff_string += b'\x01' + size + str16
        return self.rfff_value + b'\x00' + rfff_string + b'\xDF'

    def df_section(self: T) -> bytes:
        df_count = len(self.df_data)
        df_string = b''
        if df_count > 0:
            df_string = (0).to_bytes(4, "little")
            for df in self.df_data:
                df_string += struct.pack("<iIHH", df[0], df[1], df[2], df[3])
        return df_count.to_bytes(2, "little") + df_string

    def four_five_offset(self: T) -> int:
        return 0xD4 + len(self.declaration_table) + len(self.guids_extra) * 16

    def df_offset(self: T) -> int:
        return self.four_five_offset() + 28

    def object_table_offset(self: T) -> int:
        """
        The object table offset is 8A less than the position.
        The object table is between the block of F's and the
        Utf-16 Guid.
        """
        return 0x017A + len(self.guids_extra) * 16

    def id_table_offset(self: T) -> int:
        """
        the offset for the byte that follows the UTF-16 GUiD
        """
        guid_len = 2 if len(self.guid) == 0 else 6 + len(self.guid) * 76
        return (self.object_table_offset() + 4 + len(self.object_table)
                + 8 + guid_len)

    def rfff_offset(self: T) -> int:
        return self.id_table_offset() + 4 + len(self.indirect_table) + 0x8E

    def second_df_offset(self: T) -> int:
        df_data_len = len(self.df_data)
        if df_data_len == 0:
            return -1
        rf_len = 6
        for rf in self.rfff_data:
            rf_len += len(rf) * 2 + 3

        return self.rfff_offset() + rf_len + 1

    def magic_offset(self: T) -> int:
        """
        0x3C before the 0xCAFE tag
        """
        if self.second_df_offset() > 0:
            return self.second_df_offset() + 12 + 58 - self.zeroes
        else:
            return self.rfff_offset() + 7

    def end_offset(self: T) -> int:
        return (self.magic_offset() + 0x3C + 16 + len(self.pcode)
                + len(self.pcode_dir))

    def _create_pcode(self: T) -> bytes:
        num = len(self.pcode_dir) // 12
        pcode = struct.pack("<HHH", 0xCAFE, 1, num)
        for i in range(num):
            pass
        pcode += self.pcode_dir
        pcode += struct.pack("<iH", -1, 0x0101)
        pcode += len(self.pcode).to_bytes(4, "little")
        pcode += self.pcode
        pcode += struct.pack("iH", -1, 0)
        return pcode

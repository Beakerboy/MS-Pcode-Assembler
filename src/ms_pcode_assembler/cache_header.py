import struct
import ms_pcode_assembler.module_cache as mc
from typing import TypeVar


T = TypeVar('T', bound='CacheHeader')


class CacheHeader():

    def __init__(self: T, cache: mc.ModuleCache, project_cookie: int,
                 syskind: int = 2, signature: int = 0) -> None:
        self._cache = cache
        self._project_cookie = project_cookie
        self._signature = signature
        self.clear_variables()

    def clear_variables(self: T) -> None:
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0
        self.data4 = 0

    def to_bytes(self: T) -> bytes:
        cache = self._cache
        mc = cache.module_cookie
        pc = self._project_cookie
        dfo = cache.df_offset()
        ito = cache.id_table_offset()
        magic_ofs = cache.magic_offset()
        rfo = cache.rfff_offset()
        ffo = cache.four_five_offset()
        edo = cache.end_offset()
        sdo = cache.second_df_offset()
        d2 = self.data2
        return struct.pack("<BHBIII IiII IIHHHh IIHhH",
                           22, self._signature, self.data1, dfo, rfo, ffo,
                           ito, sdo, magic_ofs, edo,
                           d2, 1, pc, mc, 0, -1,
                           self.data3, self.data4, 0xB6, -1, 0x0101)

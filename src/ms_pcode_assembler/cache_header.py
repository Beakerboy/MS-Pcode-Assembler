from typing import TypeVar


T = TypeVar('T', bound='CacheHeader')


class CacheHeader():

    def __init__(self: T, cache, project_cookie: int,
                 syskind: int = 2, siganture = 0) -> None:
        self._cache = cache
        self._project_cookie = project_cookie
        self._signature = signature * 256 + 22
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0

    def clear_variables(self: T) -> None:
        self.data1 = 0
        self.data2 = 0
        self.data3 = 0

    def to_bytes(self: T) -> bytes:
        cache = self._cache
        misc = cache.misc[0]
        dfo = cache.df_offset()
        ito = cache.id_table_offset()
        magic_ofs = cache.magic_offset()
        rfo = cache.rfff_offset()
        ffo = cache.four_five_offset()
        edo = cache.end_offset()
        sdo = cache.second_df_offset()
        return struct.pack("<BIIIIIiIIIIHHHhIIHhH", 1, self.signature,
                           dfo, rfo, ffo, ito, sdo, magic_ofs,
                           edo, misc[0], 1, self._project_cookie,
                           self._module_cookie, 0, -1, misc[1],
                           misc[2], 0xB6, -1, 0x0101)

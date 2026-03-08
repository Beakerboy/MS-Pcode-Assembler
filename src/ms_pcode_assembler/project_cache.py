import struct

from typing import TypeVar


S = TypeVar('S', bound='ModuleBase')


class ModuleBase:
    def __init__(self: S) -> None:
        self.name = ""
        self.cookie = 0


T = TypeVar('T', bound='ProjectCache')


class ProjectCache():
    """
    The project cache resides in the _VBA_PROJECT_ stream.
    """
    def __init__(self: T, version: int, project_cookie: int,
                 hex: int) -> None:
        self._version = version
        self._hex = hex
        self._libraries = []
        self._modules = []
        self._project_cookie = project_cookie
        self._user = []
        self._compile = []
        self._data = []
        self._post_data = []
        self._post_f_data = []

    def add_module(self: T, module: ModuleBase) -> None:
        self._modules.append(module)

    def add_library(self: T, library: str) -> None:
        self._libraries.append(library)

    def to_bytes(self: T) -> bytes:
        ca = b'\xff'
        ca += self._header()
        ca += self._library_section()
        ca += self._user_clas_section(self._user)
        ca += self._compile_time_data()
        ca += self._data_section()
        ca += self._module_section()
        ca += self._post_module_section()
        ca += self._identifier_section()
        ca += self._footer_section()
        return ca

    def _header(self: T) -> bytes:
        return struct.pack("<IIHHIIH", 1033, 1033, self._version, 3, 0, 0, 1)

    def _library_section(self: T) -> bytes:
        ca = struct.pack("<HH", len(self._libraries), 2)

        for lib in self._libraries:
            extra = b''
            if isinstance(lib, tuple):
                text = lib[0]
                num = 1
                lib1_str = bytearray(lib[1], "utf_16_le")
                extra = struct.pack("<H", len(lib1_str))
                extra += bytearray(lib[1], "utf_16_le")
                extra += (struct.pack("<IIHHH", 0, 0, 0, num, 0) + lib[2] +
                          b'\x00\x00')
            else:
                text = lib
                num = 0
                extra = b''

            lib_str = bytearray(text, "utf_16_le")
            ca += struct.pack("<H", len(lib_str))
            ca += lib_str
            ca += struct.pack("<IIHH", 0, 0, 0, num) + extra
        return ca

    def _user_class_section(self: T) -> bytes:
        user = self._user
        ca = struct.pack("<H", len(user))
        for num in user:
            ca += struct.pack("<H", num)
        return ca

    def _compile_time_data(self: T) -> bytes:
        compile = self._compile
        ca = struct.pack("<H", len(compile))
        for num in compile:
            ca += struct.pack("<I", num)
        return ca

    def _data_section(self: T) -> bytes:
        data = self._data
        # Header?
        ca = struct.pack("<HihIHHI", data[0], -1, -1, 0, data[1], 0, self._hex)

        # 66 bytes of data
        for num in data[2:7]:
            ca += struct.pack("<h", num)
        ca += struct.pack("<ii", data[7], -1)
        for num in data[8:20]:
            ca += struct.pack("<h", num)
        ca += struct.pack("<iihhi", -1, -1, -1, data[20], -1)
        for num in data[21:25]:
            ca += struct.pack("<h", num)
        # Footer 22 bytes
        ca += struct.pack("<5IH", 1, 0, 0, 0, 0, self._project_cookie)
        return ca

    def _module_section(self: T) -> bytes:
        i = 0
        ca = struct.pack("<H", len(self._modules))

        for module in self._modules:
            name = module[0].encode("utf_16_le")
            ca += struct.pack("<H", len(name)) + name
            txt = (
                chr(module[1]) + chr(module[2]) + hex(module[3])[2:]
            ).encode("utf_16_le")
            ca += struct.pack("<H", len(txt)) + txt
            cookie = module[5]
            ca += struct.pack("<HHH", 0xFFFF, module[4], len(name)) + name
            ca += struct.pack("<HHIH", 0xFFFF, cookie, 0, len(module[7]))
            if len(module[7]) > 0:
                for num in module[7]:
                    ca += struct.pack("<Ii", num, -1)
            ca += struct.pack("<IBIh", 0x0200 + i * 24, 0,
                              module[6], module[8])
            i += 1
        return ca

    def _post_module_section(self: T) -> bytes:
        ca = struct.pack("<IH", 0xFFFFFFFF, 0x0101)

        neg_one_4b = b'\xFF\xFF\xFF\xFF'
        record = neg_one_4b * 128

        for (location, value) in self._post_f_data:
            word = struct.pack("<I", value)
            record = (f_section[:location] + word +
                         f_section[location + 4:])

        ca += f_section

        neg_one_one = neg_one_4b + struct.pack("<I", 1)
        bin_array = self._post_data

        for byte_string in bin_array:
            record += byte_string + neg_one_one

        record += neg_one_4b + struct.pack("<I", 0x30)
        ca += struct.pack("<I", len(record)) + record
        return ca

    def _identifier_section(self: T) -> bytes:
        names = [
            (0x2b80, b"Excel"), (0xe2f7, b"VBA"), (0x7ec1, b"Win16"),
            (0x7f07, b"Win32"), (0x7f78, b"Win64"), (0xb2b3, b"Mac"),
            (0x23ad, b"VBA6"), (0x23ae, b"VBA7"), (0x170a, b"Project1"),
            (0x6093, b"stdole"), (0xbfbe, b"VBAProject"), (0x7515, b"Office"),
            (0xe37c, b"ThisWorkbook"), (0xd918, b"_Evaluate", 0x103FF),
            (0x1ae8, b"Sheet1"), (0x1162, b"Module1"), (0x186b, b"Workbook")
            ]
        ca = struct.pack(
            "<IHHHHI", 0x80, 0, 0x0117, len(names), 0x0106, 0x2ba0
        )
        for name in names:
            if len(name) == 2:
                ca += struct.pack(
                    "<BB" + str(len(name[1])) + "sHH", len(name[1]), 4,
                    name[1], name[0], 16
                )
            else:
                ca += struct.pack("<BBHI" + str(len(name[1])) + "sHH",
                                  len(name[1]), 0x80, 0, name[2], name[1],
                                  name[0], 16)
        return ca

    def _footer_section(self: T) -> bytes:
        hex = ("02 FF FF 01 01 60 00 00 00 20 02",
               "02 00 FF FF 22 02 FF FF FF FF 24 02 03 00 FF FF",
               "27 02 00 00 03 00 FF FF FF FF FF FF 2B 02 01 00",
               "03 00 2D 02 02 00 05 00 0E 02 01 00 FF FF 10 02",
               "00 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
               "FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
               "FF FF FF FF FF FF FF FF FF FF FF FF FF FF 06 00",
               "10 00 00 00 01 00 36 00 00 00 00 00 00 00 00 00",
               "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
               "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
               "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        return bytes.fromhex(" ".join(hex))

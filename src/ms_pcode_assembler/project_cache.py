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

    def add_module(self: T, module: ModuleBase) -> None:
        self._modules.append(module)

    def add_library(self: T, library: str) -> None:
        self._libraries.append(library)

    def to_bytes(self: T) -> bytes:
        ca = b'\xff'
        ca += self._header()
        ca += self._library_section()
        ca += self._user_clas_section()
        ca += self._compile_time_data()
        ca += self._data_section()
        ca += self._module_section()
        ca += self._identifier_section()
        ca += self._footer_section()
        return ca

    def _header(self: T) -> bytes:
        return struct.pack("<IIHHIIH", 1033, 1033, self._version, 3, 0, 0, 1)

    def _library_section(self: T) -> bytes:
        ca = struct.pack("<HH", len(self._libraries), 2)

        for lib in self._libraries:
            if isinstance(lib, tuple):
                text = lib[0]
                num = 1
                extra = struct.pack("<H", len(lib[1])) + bytearray(lib[1], "utf_16_le")
            else:
                text = lib
                num = 0
                extra = b''
                
            lib_str = bytearray(text, "utf_16_le")
            ca += struct.pack("<H", len(lib_str))
            ca += lib_str
            ca += struct.pack("<III", 0, 0, num) + extra
        return ca

    def _user_class_section(self: T) -> bytes:
        return struct.pack("<5H", 3, 2, 2, 1, 6)

    def _compile_time_data(self: T) -> bytes:
        return struct.pack("<6IH", 0x0212,  0x010214, 0x010216, 0x0218,
                           0x01021a, 0x01021c, 0x0222)

    def _data_section(self: T) -> bytes:
        # Data
        ca = b'\xFF' * 6 + b'\x00' * 4 + b'\xFF' * 2 + b'\x00' * 2
        ca += struct.pack("<IH", self._hex, 0x11)

        # 64 bytes?
        ca += b'\xFF' * 8
        ca += struct.pack("<I", 1)
        ca += b'\xFF' * 36 + struct.pack("<H", 2) + b'\xFF' * 14

        # Footer?
        ca += struct.pack("<5IH", 1, 0, 0, 0, 0, self._proj_cookie)
        return ca

    def _module_section(self: T) -> bytes:
        ca = struct.pack("<H", len(self._modules))
        i = 0

        data_str = [0, 0, 6]
        data = [0x0227, 0x022B, 0x022C]
        # data1 = i*24
        data1 = [0, 0x18, 0x30]
        data2 = [0x0333, 0x0333, 0x0283]
        for module in self._modules:
            name = module.name.encode("utf_16_le")
            ca += struct.pack("<H", len(name)) + name
            txt = (
                "2" + chr(70 + i) + hex((self._hex + data_str[i]))[2:]
            ).encode("utf_16_le")
            ca += struct.pack("<H", len(txt)) + txt
            ca += struct.pack("<HHH", 0xFFFF, data[i], len(name)) + name
            ca += struct.pack("<HHIH", 0xFFFF, module.cookie, 0, 0)
            ca += struct.pack("<BIIH", data1[i], 2, data2[i], 0xFFFF)
            i += 1
        return ca

    def _identifier_section(self: T) -> bytes:
        ca = struct.pack("<IH", 0xFFFFFFFF, 0x0101)
        neg_one_4b = b'\xFF\xFF\xFF\xFF'
        neg_one_one = neg_one_4b + struct.pack("<I", 1)
        bin_array = [
            b'\xf1q\x9a\xee\xc0\xe0\xc4F\xa2\xf8l|\xf9{s\x06',
            b'vS\x9e\xe1B\x85\xfeF\xa1\x8b0E\x08tCU',
            b'"\x93\xba>\xc3\x82\xfcD\x88\xcav\x96\xe5\x061"'
        ]

        record = (
            neg_one_4b * 13 + struct.pack("<2I", 0x0230, 0x0218) +
            neg_one_4b * 28 + struct.pack("<I", 0x0200) + neg_one_4b * 84)
        for byte_string in bin_array:
            record += byte_string + neg_one_one

        record += neg_one_4b + struct.pack("<I", 0x30)
        ca += struct.pack("<I", len(record)) + record
        names = [
            (0x2b80, b"Excel"), (0xe2f7, b"VBA"), (0x7ec1, b"Win16"),
            (0x7f07, b"Win32"), (0x7f78, b"Win64"), (0xb2b3, b"Mac"),
            (0x23ad, b"VBA6"), (0x23ae, b"VBA7"), (0x170a, b"Project1"),
            (0x6093, b"stdole"), (0xbfbe, b"VBAProject"), (0x7515, b"Office"),
            (0xe37c, b"ThisWorkbook"), (0xd918, b"_Evaluate", 0x103FF),
            (0x1ae8, b"Sheet1"), (0x1162, b"Module1"), (0x186b, b"Workbook")
            ]
        ca += struct.pack(
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

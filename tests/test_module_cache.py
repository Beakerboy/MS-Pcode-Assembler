import struct
import uuid
from ms_pcode_assembler.module_cache import ModuleCache


def test_doc_cache():
    cache = ModuleCache(0xB5, 0x08F3)
    cache.module_cookie = 0xB81C
    cache.misc = [0x0316, 0x0123, 0x88, 8, 0x18, "00000000", 1]
    guid = uuid.UUID('0002081900000000C000000000000046')
    cache.guid = [guid]

    indirect_table = ("02 80 FE FF FF FF FF FF 20 00 00 00 FF FF FF FF",
                      "30 00 00 00 02 01 FF FF 00 00 00 00 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 2E 00 43 00",
                      "1D 00 00 00 25 00 00 00 FF FF FF FF 40 00 00 00")
    cache.indirect_table = bytes.fromhex(" ".join(indirect_table))
    object_table = ("02 00 53 4C FF FF FF FF 00 00 01 00 53 10 FF FF",
                    "FF FF 00 00 01 00 53 94 FF FF FF FF 00 00 00 00",
                    "02 3C FF FF FF FF 00 00")
    cache.object_table = bytes.fromhex(" ".join(object_table))

    f = open('tests/vbaProject.bin', 'rb')
    f.seek(0x0800)
    file_data = f.read(0x0333)
    assert cache.to_bytes() == file_data


def test_module_cache():
    cache = ModuleCache(0xB5, 0x08F3)
    cache.module_cookie = 0xB241
    cache.misc = [0x0316, 3, 0, 2, 0xFFFF, "FFFFFFFF", 0]
    cache.indirect_table = struct.pack("<iI", -1, 0x78)
    f = open('tests/vbaProject.bin', 'rb')
    f.seek(0x1200)
    file_data = f.read(0x0283)
    assert cache.to_bytes() == file_data

def test_full_cache():
    cache = ModuleCache(0xB2, 0x78B9)
    cache.module_cookie = 0x0399
    cache.misc = [0x0316, 0x0123, 0x88, 8, 0x18, "00000000", 1]
    guid = uuid.UUID('fcfb3d2aa0fa1068a73808002b3371b5')
    cache.guid = [guid]

    indirect_table = ("0C 21 32 02 78 00 00 00 01 00 03 68 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00",
                      "00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00",
                      "0A 00 00 00 00 00 00 00 58 00 00 00 0C 00 FF FF",,
                      "38 00 00 00 05 00 05 00 05 00 00 00 00 00 00 00",
                      "BC 01 00 03 00 00 00 00 69 83 FE FF FF FF FF FF",
                      "FF FF FF FF FF FF FF FF 0C 01 FF FF 00 00 00 00",
                      "FF FF FF FF 20 00 00 00 0C 41 34 02 F0 00 00 00",
                      "00 00 03 68 00 00 00 00 FF FF FF FF FF FF FF FF",
                      "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                      "FF FF FF FF 00 00 00 00 0A 00 00 00 00 00 00 00",
                      "D0 00 00 00 FF FF FF FF 40 00 01 00 05 00 05 00",
                      "0A 00 00 00 00 00 00 00 94 01 00 03 00 00 00 00",
                      "69 83 36 02 FF FF FF FF FF FF FF FF FF FF FF FF",
                      "08 01 FF FF 00 00 00 00 FF FF FF FF 80 01 00 00",
                      "0C 11 38 02 48 01 00 00 02 00 03 60 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00",
                      "00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00",
                      "0A 00 00 00 00 00 00 00 FF FF FF FF FF FF FF FF",
                      "48 00 02 00 05 00 05 00 0F 00 00 00 00 00 00 00",
                      "94 00 00 03 00 00 00 00 0C 11 3A 02 A0 01 00 00",
                      "03 00 03 60 00 00 00 00 FF FF FF FF FF FF FF FF",
                      "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00",
                      "FF FF FF FF 00 00 00 00 0A 00 00 00 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 50 00 03 00 05 00 05 00",
                      "14 00 00 00 00 00 00 00 94 00 00 03 00 00 00 00",
                      "0C 11 3C 02 FF FF FF FF 04 00 03 60 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00",
                      "00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00",
                      "0A 00 00 00 00 00 00 00 F8 01 00 00 0C 00 FF FF",
                      "58 00 04 00 04 00 04 00 19 00 00 00 00 00 00 00",
                      "BC 01 00 03 00 00 00 00 69 83 FE FF FF FF FF FF",
                      "FF FF FF FF FF FF FF FF 0C 01 FF FF 00 00 00 00",
                      "FF FF FF FF 20 00 00 00 02 80 FE FF FF FF FF FF",
                      "20 00 00 00 FF FF FF FF 48 02 00 00 02 01 FF FF",
                      "18 02 00 00 00 00 00 00 FF FF FF FF FF FF FF FF",
                      "00 00 00 00 00 00 00 00 1D 00 00 00 25 00 00 00",
                      "FF FF FF FF A0 01 00 00 00 00 00 00 FF FF FF FF",
                      "FF FF FF FF 78 00 00 00 F0 00 00 00 48 01 00 00",
                      "02 83 FE FF FF FF FF FF 00 00 00 00 FF FF FF FF",
                      "A0 02 00 00 00 00 FF FF FF FF FF FF 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 FF FF FF FF",
                      "1D 00 18 00 25 00 00 00 FF FF FF FF 50 01 00 00",
                      "FF FF FF FF A0 01 00 00")
    cache.indirect_table = bytes.fromhex(" ".join(indirect_table))
    object_table = ("02 00 53 10 FF FF FF FF 00 00 01 00 53 0C FF FF",
                    "FF FF 00 00 01 00 53 94 FF FF FF FF 00 00 00 00",
                    "36 22 FF FF FF FF 00 00")
    cache.object_table = bytes.fromhex(" ".join(object_table))

    f = open('tests/SQL-vbaProject.bin', 'rb')
    f.seek(0x1200)
    file_data = f.read(0x08C4)
    assert cache.to_bytes() == file_data

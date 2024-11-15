import struct
import uuid
from ms_pcode_assembler.module_cache import ModuleCache


def test_doc_cache() -> None:
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


def test_module_cache() -> None:
    cache = ModuleCache(0xB5, 0x08F3)
    cache.module_cookie = 0xB241
    cache.misc = [0x0316, 3, 0, 2, 0xFFFF, "FFFFFFFF", 0]
    cache.indirect_table = struct.pack("<iI", -1, 0x78)
    f = open('tests/vbaProject.bin', 'rb')
    f.seek(0x1200)
    file_data = f.read(0x0283)
    assert cache.to_bytes() == file_data

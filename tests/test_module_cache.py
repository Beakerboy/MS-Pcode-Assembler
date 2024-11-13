import struct
import uuid
from ms_pcode_assembler.module_cache import ModuleCache


def test_doc_cache() -> None:
    cache = ModuleCache(0xB5, 0x08F3)
    cache.module_cookie = 0xB81C
    cache.misc = [[0x0316, 0, 0x0123, 0x88], [-1, 8],
                  0x18, 0, [1, "00000000"]]
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
    cache.misc = [[0x0316, 0, 3, 0], [-1, 2],
                  0xFFFF, 0, [0, "FFFFFFFF"]]
    cache.indirect_table = struct.pack("<iI", -1, 0x78)
    f = open('tests/vbaProject.bin', 'rb')
    f.seek(0x1200)
    file_data = f.read(0x0283)
    assert cache.to_bytes() == file_data


def test_full_cache() -> None:
    cache = ModuleCache(0xB2, 0x78B9)
    cache.rfff_value = b'\x73\x62\xC6\x63\x07'
    cache.module_cookie = 0x0399
    cache.zeroes = 56
    misc = [[0x6000316, 5, 3, 0x80], [0x70, 8],
            0xFFFF, 7, [1, "18020000"]]
    cache.misc = misc
    guid = uuid.UUID('fcfb3d2aa0fa1068a73808002b3371b5')
    cache.guid = [guid]

    guid1 = uuid.UUID(bytes_le=b'\xA6\xB1\x2C\xB6\x36\x4E\x61\x47' +
                               b'\xB9\xB2\xB7\x24\x66\x0C\x9F\xA6')
    guid_zero = uuid.UUID(int=0x0)
    cache.guids1 = [guid1, guid, guid_zero]
    guid2 = uuid.UUID(bytes_le=b'\xAA\x36\x92\xBE\x96\xC1\xA5\x47' +
                               b'\x81\xD2\xCF\xA6\x4F\x5A\x18\xE2')
    cache.guids_extra = [guid2]
    cache.guids2 = [guid2, guid1]
    cache.rfff_data = ['*\\Rffff*2363c69a74']
    cache.df_data = [[-1, 0x60, 5, 0]]
    f_data = ("05 00 05 00 00 00 01 00 00 00 00 00 00 00 00 00",
              "00 00 00 00 FF FF FF FF FF FF FF FF" + misc[3],
              "FF FF FF FF FF FF FF FF A0 01 00 00 FF FF FF FF",
              "FF FF FF FF" + misc[3] + "FF FF FF FF FF FF FF FF",
              "FF FF FF FF FF FF FF FF 70 02 00 00 00 00 00 00",
              "00 00 00 00 78 00 00 00 08 00 00 00 00 00 60 00",
              "38 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF",
              "FF FF FF FF FF FF FF FF 10 00 00 00 08 00 B0 02",
              "00 00")
    cache.f_data = bytes.fromhex(" ".join(f_data))
    indirect_table = ("0C 21 32 02 78 00 00 00 01 00 03 68 00 00 00 00",
                      "FF FF FF FF FF FF FF FF 00 00 00 00 00 00 00 00",
                      "00 00 00 00 00 00 00 00 FF FF FF FF 00 00 00 00",
                      "0A 00 00 00 00 00 00 00 58 00 00 00 0C 00 FF FF",
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
                      "FF FF FF FF A0 01 00 00 00 00 00 00 FF FF FF FF",
                      "FF FF FF FF 78 00 00 00 F0 00 00 00 48 01 00 00",
                      "FF FF FF FF 88 02 00 00 ")
    cache.indirect_table = bytes.fromhex(" ".join(indirect_table))
    object_table = ("02 00 53 10 FF FF FF FF 00 00 01 00 53 0C FF FF",
                    "FF FF 00 00 01 00 53 94 FF FF FF FF 00 00 00 00",
                    "36 22 FF FF FF FF 00 00")
    cache.object_table = bytes.fromhex(" ".join(object_table))
    pcode_dir = ("00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 20 00 00 00 00 00 00 00",
                 "00 80 09 00 44 00 00 00 20 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 1C 00 00 00 68 00 00 00",
                 "42 A1 0C 00 06 00 10 00 88 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "04 81 08 00 02 00 00 00 90 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 22 00 00 00 98 00 00 00",
                 "22 A1 0C 00 06 00 10 00 C0 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "04 81 08 00 02 00 00 00 C8 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 1A 00 00 00 D0 00 00 00",
                 "22 81 08 00 06 00 10 00 F0 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "04 81 08 00 02 00 00 00 F8 00 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 1C 00 00 00 00 01 00 00",
                 "22 81 08 00 06 00 10 00 20 01 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "04 81 08 00 02 00 00 00 28 01 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "00 80 09 00 16 00 00 00 30 01 00 00",
                 "42 81 0C 00 06 00 10 00 48 01 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF",
                 "04 81 08 00 02 00 00 00 50 01 00 00",
                 "00 80 09 00 00 00 00 00 FF FF FF FF")
    cache.pcode_dir = bytes.fromhex(" ".join(pcode_dir))

    pcode = ("E3 00 00 00 1A 00 20 49 6E 74 65 72 66 61 63 65",
             "3A 20 69 53 51 4C 43 6F 6E 6E 65 63 74 69 6F 6E",
             "E3 00 00 00 3D 00 20 44 65 66 69 6E 65 73 20 61",
             "20 77 72 61 70 70 65 72 20 66 6F 72 20 61 20 63",
             "75 73 6F 6D 20 63 6F 6E 6E 65 63 74 69 6F 6E 20",
             "6F 72 20 41 44 4F 44 42 2E 43 6F 6E 6E 65 63 74",
             "69 6F 6E 00 00 00 00 00",
             "E3 00 00 00 15 00 20 50 72 6F 70 65 72 74 79 3A",
             "20 43 6F 6E 6E 65 63 74 69 6F 6E 00 78 00 00 00",
             "96 18 00 00 00 00 00 00",
             "6D 00 FF FF 68 00 00 00",
             "E3 00 00 00 1B 00 20 50 72 6F 70 65 72 74 79 3A",
             "20 43 6F 6E 6E 65 63 74 69 6F 6E 53 74 72 69 6E",
             "67 00 00 00 00 00 00 00",
             "96 14 78 00 00 00 00 00",
             "6D 00 FF FF 30 00 00 00",
             "E3 00 00 00 14 00 20 53 75 62 3A 20 4F 70 65 6E",
             "43 6F 6E 6E 65 63 74 69 6F 6E 00 00 00 00 00 00",
             "96 14 F0 00 00 00 00 00",
             "6F 00 FF FF 00 00 00 00",
             "E3 00 00 00 15 00 20 53 75 62 3A 20 43 6C 6F 73",
             "65 43 6F 6E 6E 65 63 74 69 6F 6E 00 00 00 00 00",
             "96 14 48 01 00 00 00 00 6F 00 FF FF D0 00 00 00",
             "E3 00 00 00 10 00 20 46 75 6E 63 74 69 6F 6E 3A",
             "20 53 74 61 74 65 00 00",
             "96 18 A0 01 00 00 00 00 69 00 FF FF A8 00 00 00",
             "FF FF FF FF A0 00 00 00")
    cache.pcode = bytes.fromhex(" ".join(pcode))
    f = open('tests/SQL-vbaProject.bin', 'rb')
    f.seek(0x1200)
    he = cache.header_section()
    file_data = f.read(len(he))
    assert he == file_data
    dt = cache.declaration_table_section()
    file_data = f.read(len(dt))
    assert dt == file_data
    gu = cache.guid_section()
    file_data = f.read(len(gu))
    assert gu == file_data
    four_five = cache.four_five_section()
    file_data = f.read(len(four_five))
    assert four_five == file_data
    ob = cache.object_table_section()
    file_data = f.read(len(ob))
    assert ob == file_data
    gu16 = cache.utf16_guid_section()
    file_data = f.read(len(gu16))
    assert gu16 == file_data
    id = cache.indirect_table_section()
    file_data = f.read(len(id))
    assert id == file_data
    fs = cache.f_section()
    file_data = f.read(len(fs))
    # fails
    # assert fs == file_data
    rf = cache.rff_section()
    file_data = f.read(len(rf))
    assert rf == file_data
    df = cache.df_section()
    file_data = f.read(len(df))
    assert df == file_data
    file_data = f.read(56)
    assert b'\x00' * 56 == file_data
    f.close()
    f = open('tests/SQL-vbaProject.bin', 'rb')
    f.seek(0x1200)
    file_data = f.read(0x08C4)
    assert cache.to_bytes() == file_data

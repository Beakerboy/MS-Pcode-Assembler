# import struct
# import uuid
from ms_pcode_assembler.project_cache import ProjectCache


def test_doc_cache() -> None:
    cache = ProjectCache(0x04e4, 0, 0)
    cache.add_library(
        "*\G{000204EF-0000-0000-C000-000000000046}#4.2#9#" +
        "C:\Program Files\Common Files\Microsoft Shared\VBA\VBA7.1\VBE7.DLL#" +
        "Visual Basic For Applications)"
    )

    f = open('tests/SQL-vbaProject.bin', 'rb')
    f.seek(0x30207)
    file_data = f.read(1)
    assert b'\xff' == file_data
    he = cache._header()
    file_data = f.read(len(he))
    assert he == file_data
    li = cache._library_section()
    file_data = f.read(len(he))
    assert li == file_data
    

# import struct
# import uuid
from ms_pcode_assembler.project_cache import ProjectCache


def test_doc_cache() -> None:
    cache = ProjectCache(0x04e4, 0x78b9, 0)
    cache.add_library(
        "*\\G{000204EF-0000-0000-C000-000000000046}#4.2#9#" +
        "C:\\Program Files\\Common Files\\Microsoft Shared" +
        "\\VBA\\VBA7.1\\VBE7.DLL#" +
        "Visual Basic For Applications"
    )
    cache.add_library(
        "*\\G{00020813-0000-0000-C000-000000000046}#1.9#0#" +
        "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE" +
        "#Microsoft Excel 16.0 Object Library"
    )
    cache.add_library(
        "*\\G{00020430-0000-0000-C000-000000000046}#2.0#0#" +
        "C:\\Windows\\System32\\stdole2.tlb#OLE Automation"
    )
    cache.add_library(
        "*\\G{2DF8D04C-5BFA-101B-BDE5-00AA0044DE52}#2.8#0#" +
        "C:\\Program Files\\Common Files\\Microsoft Shared" +
        "\\OFFICE16\\MSO.DLL" +
        "#Microsoft Office 16.0 Object Library"
    )
    lib = ("*\\G{0D452EE1-E08F-101A-852E-02608C4D0BB4}#2.0#0#" +
           "C:\\WINDOWS\\system32\\FM20.DLL#" +
           "Microsoft Forms 2.0 Object Library")
    child = ("*\\G{3AF3885D-1EAB-4BD6-A2CF-8C849267EC75}#2.0#0#" +
             "C:\\Users\\KNOWAC~1\\AppData\\Local\\Temp\\VBE\\MSForms.exd#" +
             "Microsoft Forms 2.0 Object Library")
    ex = b'\xe1\x2EE\x0D\x8F\xE0\x1A\x10\x85\x2E\x02\x60\x8CM\x0B\xB4'
    cache.add_library((lib, child, ex))

    cache.add_library(
        "*\\G{B691E011-1797-432E-907A-4D8C69339129}#6.1#0#" +
        "C:\\Program Files\\Common Files\\System\\ado\\msado15.dll#" +
        "Microsoft ActiveX Data Objects 6.1 Library"
    )
    cache.add_library(
        "*\\G{420B2830-E718-11CF-893D-00A0C9054228}#1.0#0#" +
        "C:\\Windows\\System32\\scrrun.dll#Microsoft Scripting Runtime"
    )
    cache._user = [2, 2, 2, 2, 2, 0x402, 0x402, 0x402, 2, 2, 2,
                   0x402, 0x402, 0x402, 2, 2, 0x402, 2, 2, 1, 1, 0x402]
    cache._compile = [0x0212, 0x10214, 0x10216, 0x218, 0x1021a, 0x1021c]
    cache._data = [0x21e, 0, 7, 14, 18, -1, 5, -1, 4, 2, 8, -1, 11, 16,
                   10, 3, 20, 12, 6, 13, 15, 17, 7, 9, 19]
    hex1 = 0x63c41a11
    hex2 = 0x63c69a74
    cache._hex = 0x63c66273
    cache._modules = [
        ("ThisWorkbook", 48, 91, hex1, 0x22b, 0xc472, 0x33b, []),
        ("Sheet1", 48, 93, hex1, 0x22f, 0xd62a, 0x33b, []),
        ("iSQLConnection", 50, 51, hex2, 0x231, 0x0399, 0x8c4, []),
        ("iSQLQuery", 50, 53, hex2, 0x23f, 0x65b5, 0x55c, []),
        ("iSQLRecordset", 50, 52, hex2, 0x243, 0xccb4, 0x9f8, []),
        ("SQLCondition", 50, 57, hex2, 0x255, 0x8c74, 0xbc8, []),
        ("SQLConnection", 50, 74, hex2, 0x267, 0x360f, 0xbed, [0x0230]),
        ("SQLCreate", 50, 71, hex2, 0x277, 0x9bce, 0x7b6, [0x0248, 0x0308]),
        ("SQLDatabase", 50, 50, hex2, 0x289, 0xac50, 0x279b,
         [0x230, 0x260, 0x248, 0x2F0, 0x338, 0x290, 0x320]),
        ("SQLDelete", 50, 70, hex2, 0x2c7, 0xc472, 0x33b,
         [0x248, 0x308, 0x30B]),
        ("SQLInsert", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLQuery", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLQueryGroup", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLRecordset", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLSelect", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLStaticQuery", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLSubselect", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLUpdate", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLWhere", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLFactory", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("SQLHelperFunctions", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
        ("Login", 50, 51, hex2, 0x22b, 0xc472, 0x33b, []),
    ]
    f = open('tests/SQL-vbaProject.bin', 'rb')
    f.seek(0x30207)
    file_data = f.read(1)
    assert b'\xff' == file_data
    he = cache._header()
    file_data = f.read(len(he))
    assert he == file_data
    li = cache._library_section()
    file_data = f.read(len(li))
    assert li == file_data
    uc = cache._user_class_section()
    file_data = f.read(len(uc))
    assert uc == file_data

    ca = cache._compile_time_data()
    file_data = f.read(len(ca))
    assert ca == file_data

    # This sector ends at 31200 and restarts at 2F200
    ca = cache._data_section()
    file_data = f.read(len(ca))
    assert ca == file_data

    ca = cache._module_section()
    file_data = f.read(0x6A0)
    f.seek(0x2F200)
    file_data += f.read(len(ca) - len(file_data))
    assert ca == file_data

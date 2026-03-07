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
        ("ThisWorkbook", 48, 91, hex1, 0x22b, 0xc472, 0x33b, [], -1),
        ("Sheet1", 48, 93, hex1, 0x22f, 0xd62a, 0x33b, [], -1),
        ("iSQLConnection", 50, 51, hex2, 0x231, 0x0399, 0x8c4, [], -1),
        ("iSQLQuery", 50, 53, hex2, 0x23f, 0x65b5, 0x55c, [], -1),
        ("iSQLRecordset", 50, 52, hex2, 0x243, 0xccb4, 0x9f8, [], -1),
        ("SQLCondition", 50, 57, hex2, 0x255, 0x8c74, 0xbc8, [], -1),
        ("SQLConnection", 50, 74, hex2, 0x267, 0x360f, 0xbed, [0x0230], -1),
        ("SQLCreate", 50, 71, hex2, 0x277, 0x9bce, 0x7b6,
         [0x0248, 0x0308], -1),
        ("SQLDatabase", 50, 50, hex2, 0x289, 0xac50, 0x279b,
         [0x230, 0x260, 0x248, 0x2F0, 0x338, 0x290, 0x320], -1),
        ("SQLDelete", 50, 70, hex2, 0x2c7, 0x87aa, 0x12d9,
         [0x248, 0x308, 0x3b0], 0),
        ("SQLInsert", 50, 54, hex2, 0x2b7, 0x9113, 0x1e8d,
         [0x248, 0x350, 0x3e0], -1),
        ("SQLQuery", 50, 56, hex2, 0x27b, 0x6bdc, 0x2001,
         [0x278, 0x3b0, 0x3e0], -1),
        ("SQLQueryGroup", 50, 75, hex2, 0x2c1, 0xab66, 0xc58, [0x248], -1),
        ("SQLRecordset", 50, 73, hex2, 0x297, 0xfa18, 0x0d45, [0x260], -1),
        ("SQLSelect", 50, 60, hex2, 0x2e7, 0x5ac7, 0x5635,
         [0x248, 0x308, 0x278, 0x3b0, 0x3e0], 21),
        ("SQLStaticQuery", 50, 67, hex2, 0x399, 0x652f, 0xfde,
         [0x248, 0x308], -1),
        ("SQLSubselect", 48, 108, hex1, 0x39d, 0x9e42, 0x9f5, [], -1),
        ("SQLUpdate", 50, 72, hex2, 0x3ab, 0x4cc5, 0x189e,
         [0x248, 0x308, 0x3b0], 1),
        ("SQLWhereGroup", 50, 59, hex2, 0x2db, 0x3e8c, 0x1662,
         [0x278], -1),
        ("SQLFactory", 50, 69, hex2, 0x3c8, 0xb67d, 0x1227,
         [0x2c0, 0x2f0, 0x350, 0x2d8, 0x2a8, 0x398, 0x368], -1),
        ("SQLHelperFunctions", 50, 76, hex2, 0x3d8, 0xac1b, 0x3e0, [], -1),
        ("Login", 48, 113, hex1, 0x403, 0x5c7c, 0x3f8, [], -1),
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

    ca = cache._data_section()
    file_data = f.read(len(ca))
    assert ca == file_data

    # This sector ends at 31200 and restarts at 2F200
    ca = cache._module_section()
    file_data = f.read(0x6AA)
    f.seek(0x2F200)
    file_data += f.read(len(ca) - len(file_data))
    assert ca == file_data

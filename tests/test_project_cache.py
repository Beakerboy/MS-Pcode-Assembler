# import struct
# import uuid
from ms_pcode_assembler.project_cache import ProjectCache


def test_doc_cache() -> None:
    cache = ProjectCache(0x04e4, 0, 0)
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
    cache.add_library((lib, child))

    cache.add_library(
        "*\\G{B691E011-1797-432E-907A-4D8C69339129}#6.1#0#" +
        "C:\\Program Files\\Common Files\\System\\ado\\msado15.dll#" +
        "Microsoft ActiveX Data Objects 6.1 Library"
    )
    cache.add_library("")
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

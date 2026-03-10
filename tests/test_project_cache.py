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
        ("SQLHelperFunctions", 50, 76, hex2, 0x3d8, 0xac1b, 0x1843, [], -1),
        ("Login", 48, 113, hex1, 0x403, 0x5c7c, 0x6d3, [], -1),
    ]
    cache._post_f_data = [
        (0x06, 0x308), (0x0a, 0x3f8), (0x0d, 0x368), (0x14, 0x338),
        (0x14, 0x338), (0x18, 0x3c8), (0x20, 0x2a8), (0x25, 0x278),
        (0x29, 0x350), (0x2d, 0x398), (0x35, 0x2d8), (0x40, 0x2c0),
        (0x43, 0x260), (0x45, 0x3b0), (0x54, 0x380), (0x5c, 0x248),
        (0x70, 0x2f0), (0x74, 0x200), (0x78, 0x3e0)
    ]

    cache._post_data = [
        b'\xdd\xfa\xde<\xcb\x87\x03F\xb1\xd0\x15\xf7\x17\xf5\x8cA',
        b'\x14\x7F\xB2\xB2\xAA\x9C]L\x9E\xD7L\x05\xD3\xC2\xFDg',
        b'\x93\x92-\xcd6\xcf=B\xa4u\xb3\x1b6J\x1e\x15',
        b'\x11\xcfj\x01\xdb?\xd1K\xac\xf2\x182\xb5\xed\xac\x02',
        b'\x9d\xde\xe4\xea\x81\x8b\xe7J\xbdxQ\xdf\x16<&\x80',
        b'\xae\x98r\xb4\xa1o\x02I\xb7\x7f\xda\xeb\xdd\x10j\x97',
        b'\x16B\xca`\xdd\xf7\xb1N\x80)\xc0\x83\x921K\x81',
        b'\xd9\xf4\x13\xdax\xac\x03C\xb2K\xa3,\xc2\x9d\xc2\x8f',
        b')\x15\x91\xec\x81\xcc\x01J\x95[$\x04"]\xeb.',
        b'\x959\xd2\xeb\xbe\xa8TK\x9c\xc1B\x8eC\x85\x85\x87',
        b'\xf6\x8c}Ej\xf7\xcfD\xbf)\x9c|B\x9c\xbf\x12',
        b'(W\xa6Ix\xf5\x0bG\x8a\x94u\xfe\x9f(\x1bE',
        (b'u\x8bk\xfc\x0e8\x12E\x8a\xa2\xdaEK\xb2\x93C', 0x230),
        b'\x08\xcb\xbf\xc2\x99K<B\xa9\xf6\xad\xde\xc1vC\xf6',
        (b'\x86);\xd4j\x0e\xb2H\x89\xb8\xfe5\xccL\xf7\xde', 0x290),
        b'6\x17p\x11o\x8c\xf7G\xad\xbe\x99\x9f\xa4\x88C\x90',
        b'\x17\xa97o\xa9\x9cJH\xa2bl\x15\xe8S\xb1\x11',
        (b'c\x88$\x00\xde;:C\xb4>\xc8\x81\xf2\x0f\x808', 0x218),
        b'fa\xeaz\xb53:K\x8a\xf3\xde*\xeaA\xf8\x91',
        b'\x03T\xb7\xf9\x87H\x98I\xac\xfb\x03%\xf9\xe5\xe5\xe0',
        b'I<X\x1dYq\xfeI\xbd\x02\xc7\xc2i\xbd]\x94',
        (b'\xca\xef\xfa\xd5\x1d\xaf\xe0B\x89\x9e\xdc\xcb\x03U\x91\xa0',
         0x320)
    ]
    cache._post_footer = 0xe8
    cache._w0 = 0x222
    cache._w2 = 0x59a4
    cache._identifiers = [
        (b'as', 128, 9, 20, 3), (b'else', 128, 68, 20, 3),
        (b'Elseif', 128, 69, 20, 3), (b'If', 128, 95, 20, 3),
        (b'Implements', 132, 97, 12, 3), (b'Line', 4, 115),
        (b'public', 128, 149, 20, 3), (b'Sub', 128, 175, 20, 3),
        (b'Excel', 12, 0x2b80), (b'VBA', 12, 0xe2f7), (b'Win16', 4, 0x7ec1),
        (b'Win32', 4, 0x7f07), (b'Win64', 4, 0x7f78), (b'Mac', 4, 0xb2b3),
        (b'VBA6', 4, 0x23ad), (b'VBA7', 4, 0x23ae), (b'SQLlib', 12, 0xc7db),
        (b'stdole', 8, 0x6093), (b'Office', 8, 0x7515),
        (b'MSForms', 8, 0x0f43), (b'ADODB', 8, 0xb273),
        (b'Scripting', 8, 0xdf8A), (b'ThisWorkbook', 12, 0xe37c),
        (b'_Evaluate', 128, 0xd918, 0, 0x103), (b'Sheet1', 12, 0x1ae8),
        (b'iSQLConnection', 12, 0xc813), (b'Connection', 4, 0xd8da),
        (b'ConnectionString', 4, 0xf2bd), (b'sConnection', 4, 0x8aa5),
        (b'OpenConnection', 4, 0xd005), (b'CloseConnection', 4, 0x74e5),
        (b'State', 4, 0x6f9),
        (b'iSQLQuery', 12, 0x73DB),
        (b'toString', 4, 0x89A8),
        (b'iSQLRecordset', 12, 0xF2FE),
        (b'OpenRecordset', 4, 0x7CD5),
        (b'MyQuery', 4, 0xDF2C),
        (b'CloseRecordset', 4, 0xF631),
        (b'GetValue', 4, 0x5D1F),
        (b'MyFieldname', 4, 0xFC6A),
        (b'GetRows', 4, 0x9FC3),
        (b'num', 4, 0xBAFA),
        (b'EOF', 4, 0x89F4),
        (b'SQLCondition', 12, 0xDB2F),
        (b'sExpression1', 4, 0x5413),
        (b'sExpression2', 4, 0x5414),
        (b'sOperator', 4, 0xB098),
        (b'Operator', 4, 0x966B),
        (b'Create', 4, 0x4DBE),
        (b'Expression1', 4, 0xDD0B),
        (b'Expression2', 4, 0xDD0C),
        (b'OperatorString', 4, 0x23B5),
        (b'SQLConnection', 12, 0xF41C),
        (b'ocnt', 4, 0xC374),
        (b'Class_Initialize', 4, 0x1B6E),
        (b'iSQLConnection_Connection', 4, 0x9973),
        (b'iSQLConnection_OpenConnection', 4, 0xD2F8),
        (b'iSQLConnection_CloseConnection', 4, 0x08F6),
        (b'iSQLConnection_State', 4, 0xD872),
        (b'iSQLConnection_ConnectionString', 4, 0xE03D),
        (b'SQLCreate', 12, 0x46C2),
        (b'oSQL', 4, 0x192C),
        (b'SQLQuery', 12, 0xF055),
        (b'AddArgument', 4, 0xAEA1),
        (b'sName', 4, 0x6403),
        (b'vValue', 4, 0x68B9),
        (b'iSQLQuery_ToString', 4, 0x8FE8),
        (b'return_string', 4, 0x6599),
        (b'ReplaceArguments', 4, 0x59C3),
        (b'SQLDatabase', 12, 0x869F),
        (b'sDSN', 4, 0xE037),
        (b'sUid', 4, 0x3965),
        (b'sPwd', 4, 0x2089),
        (b'cnt', 4, 0x7F2B),
        (b'rst', 4, 0xD01B),
        (b'sType', 4, 0x7159),
        (b'SQLRecordset', 12, 0x1B65),
        (b'DSN', 4, 0x8537),
        (b'sValue', 4, 0x2497),
        (b'DBType', 4, 0x453A),
        (b'Username', 4, 0xE65C),
        (b'Password', 4, 0xCEF0),
        (b'MyConnection', 4, 0xE87B),
        (b'Recordset', 4, 0xE6DA),
        (b'MyRecordset', 4, 0xC97A),
        (b'MakeConnectionString', 4, 0x6C65),
        (b'Execute', 4, 0xCD59),
        (b'return_column', 4, 0xBF0F),
        (b'sSQL', 4, 0x2FE3),
        (b'SQLType', 4, 0xB8CD),
        (b'adStateOpen', 0x00, 0x3D9B),
        (b'InsertGetNewId', 4, 0x2EB3),
        (b'SQLInsert', 12, 0x6BDA),
        (b'ReturnColumn', 4, 0x34DF),
        (b'PrepareInsert', 4, 0x3847),
        (b'stSQL', 4, 0x66D3),
        (b'MySQLGroup', 4, 0xED72),
        (b'SQLQueryGroup', 12, 0xF994),
        (b'AddQuery', 4, 0x283F),
        (b'Returning', 4, 0x17EA),
        (b'SQLDelete', 12, 0x71BC),
        (b'sTable', 4, 0xCA34),
        (b'Table', 4, 0xF181),
        (b'AddWhere', 4, 0xF82F),
        (b'Field', 4, 0x33FC),
        (b'Value', 4, 0x4BE4),
        (b'op', 4, 0x5E90),
        (b'GroupType', 4, 0x08BC),
        (b'AddWhereGroup', 4, 0x2D0B),
        (b'NewWhereGroup', 4, 0x5314),
        (b'SQLWhereGroup', 12, 0x396D),
        (b'WhereString', 4, 0xA126),
        (b'vFields', 4, 0xFA35),
        (b'sReturning', 4, 0xBFCF),
        (b'vValues', 4, 0x6DC1),
        (b'MySelect', 4, 0xCD89),
        (b'SQLSelect', 12, 0xB440),
        (b'Fields', 4, 0xA937),
        (b'Values', 4, 0x1CC3),
        (b'From', 4, 0x207E),
        (b'ReturnString', 4, 0xDBA8),
        (b'ImplodeFields', 4, 0xCEE5),
        (b'ImplodeValues', 4, 0x32F0),
        (b'IsArray', 0x00, 0x959C),
        (b'JoinArrayofArrays', 0xAC, 0xCFC1, 0x128, 0x00),
        (b'Join', 0x00, 0x264D),
        (b'dArguments', 4, 0xA448),
        (b'Dictionary', 0x00, 0x81BB),
        (b'oWhere', 4, 0x0BB1),
        (b'oWhereGroup', 4, 0x2ECD),
        (b'Arguments', 4, 0x7D6A),
        (b'NewWhere', 4, 0xC194),
        (b'SetGroup', 4, 0xEA01),
        (b'ClearArguments', 4, 0x17CB),
        (b'VarType', 0x00, 0x70AF),
        (b'vbString', 0x00, 0x6560),
        (b'str', 0xAC, 0xD597, 0x1401, 0x00),
        (b'sQuery', 4, 0x96D8),
        (b'dPosition', 4, 0x0D8D),
        (b'aToSort', 4, 0x6111),
        (b'iDictSize', 4, 0x0F03),
        (b'Count', 0x00, 0x7630),
        (b'sKey', 4, 0x0368),
        (b'Position', 4, 0xDD1B),
        (b'Keys', 0x00, 0xB871),
        (b'QuickSort', 0xAC, 0xEA8C, 0x128, 0x00),
        (b'ExtraChars', 4, 0xB28A),
        (b'vPosition', 4, 0x9595),
        (b'Replace', 0x00, 0x0E66),
        (b'sWhere', 4, 0x6689),
        (b'aQueries', 4, 0xBB33),
        (b'iLength', 0x00, 0xEFBF),
        (b'orst', 4, 0x1425),
        (b'iSQLRecordset_State', 4, 0x2E06),
        (b'iSQLRecordset_OpenRecordset', 4, 0xC288),
        (b'iSQLRecordset_CloseRecordset', 4, 0x34DE),
        (b'iSQLRecordset_GetValue', 4, 0x4322),
        (b'iSQLRecordset_GetRows', 4, 0xAB3C),
        (b'iSQLRecordset_EOF', 4, 0x09D5),
        (b'bDistinct', 4, 0xC1D6),
        (b'vGroupBy', 4, 0x20D4),
        (b'oHaving', 4, 0xF395),
        (b'oHavingGroup', 4, 0x4BCB),
        (b'aJoin', 4, 0x552B),
        (b'aOrder', 4, 0x8259),
        (b'sUnion', 4, 0x8BAC),
        (b'addTable', 4, 0x5B9B),
        (b'element', 4, 0x1F5B),
        (b'AddField', 4, 0x9E55),
        (b'GroupBy', 4, 0x408F),
        (b'sField', 4, 0x0CAF),
        (b'sAlias', 4, 0x9820),
        (b'ArrLen', 4, 0x62C6),
        (b'AddHaving', 4, 0xD33A),
        (b'NewHaving', 4, 0x74C3),
        (b'AddJoin', 4, 0xCC3C),
        (b'sCondition', 4, 0x4E0B),
        (b'JoinLen', 4, 0xCC00),
        (b'InnerJoin', 4, 0x7154),
        (b'LeftJoin', 4, 0xF0F9),
        (b'RightJoin', 4, 0xEB39),
        (b'Union', 4, 0xB2F9),
        (b'oSelect', 4, 0x6507),
        (b'UnionArray', 4, 0xFB9B),
        (b'Distinct', 4, 0x552E),
        (b'bValue', 4, 0xA2FF),
        (b'OrderBy', 4, 0x9A14),
        (b'sDirection', 4, 0xDE47),
        (b'getByProperty', 4, 0xD51D),
        (b'sTableValue', 4, 0xB10C),
        (b'sProperty', 4, 0xFCA4),
        (b'DistinctString', 4, 0x5122),
        (b'FieldList', 4, 0xBA04),
        (b'JoinString', 4, 0x0B21),
        (b'GroupByString', 4, 0xE17D),
        (b'HavingString', 4, 0x558A),
        (b'OrderByString', 4, 0x46E0),
        (b'sDistinct', 4, 0x6F5B),
        (b'R', 4, 0x1069),
        (b'Lines', 4, 0xCEBA),
        (b'LineArray', 4, 0x984A),
        (b'sHaving', 4, 0xF298),
        (b'UnionString', 4, 0x336E),
        (b'NewSelect', 4, 0xE674),
        (b'aUnion', 0x00, 0xF35E),
        (b'SQLStaticQuery', 12, 0x398E),
        (b'Query', 4, 0xBE25),
        (b'SQLSubselect', 12, 0x7D84),
        (b'sAs', 4, 0xD2D9),
        (b'SelectSQL', 4, 0xE41C),
        (b'oValue', 4, 0xC9FE),
        (b'SelectAs', 4, 0xA2D4),
        (b'aAs', 0x00, 0x7297),
        (b'MySQLQuery', 4, 0xBBAF),
        (b'SQLUpdate', 12, 0xE655),
        (b'FieldsAndValues', 4, 0x0994),
        (b'numfields', 4, 0x89D7),
        (b'vFieldsAndValues', 4, 0x1E65),
        (b'counter', 4, 0x16FB),
        (b'Where1', 4, 0xA264),
        (b'Where2', 4, 0xA265),
        (b'WhereGroup1', 4, 0x5C49),
        (b'WhereGroup2', 4, 0x5C4A),
        (b'BoolOperator', 4, 0xDAFC),
        (b'oWhere1', 4, 0x3CAE),
        (b'oWhere2', 4, 0x3CAF),
        (b'MsgBox', 0x00, 0x5297),
        (b'sWhere1', 4, 0x3BB1),
        (b'sWhere2', 4, 0x3BB2),
        (b'SQLFactory', 12, 0xED5F),
        (b'Create_SQLDatabase', 0xAC, 0x4DB8, 0x128, 0x00),
        (b'Create_SQLInsert', 0xAC, 0xC4AC, 0x128, 0x00),
        (b'Create_SQLSelect', 0xAC, 0x1C54, 0x128, 0x00),
        (b'Create_SQLDelete', 0xAC, 0xCA8E, 0x128, 0x00),
        (b'Create_SQLCreate', 0xAC, 0x9F94, 0x128, 0x00),
        (b'Create_SQLUpdate', 0xAC, 0x4E69, 0x128, 0x00),
        (b'Create_SQLStaticQuery', 0xAC, 0x0DD7, 0x128, 0x00),
        (b'SQLHelperFunctions', 12, 0xDD76),
        (b'toUnix', 0xAC, 0xB88A, 0x128, 0x00),
        (b'dt', 4, 0x5CFD),
        (b'DateDiff', 0x00, 0xEAA1),
        (b'toISO', 0xAC, 0xE75E, 0x128, 0x00),
        (b'vArray', 4, 0xAE58),
        (b'WordDelim', 4, 0xA81E),
        (b'LineDelim', 4, 0x253A),
        (b'vbNewLine', 0x00, 0x6175),
        (b'InnerArray', 4, 0x384E),
        (b'getDimension', 0xAC, 0xD7FC, 0x128, 0x00),
        (b'Var', 4, 0xE2E3), (b'Err', 4, 0x8A6F),
        (b'i', 4, 0x1060), (b'tmp', 4, 0xD9EB),
        (b'inLow', 4, 0xEC29), (b'inHi', 4, 0x5B2C),
        (b'pivot', 4, 0x426C), (b'tmpSwap', 4, 0x1B17),
        (b'tmpLow', 4, 0xAE84), (b'tmpHi', 4, 0x7FB5),
        (b'Login', 12, 0x4BCD), (b'Ready', 4, 0xDDEC),
        (b'Form_Load', 4, 0x7B1D),
        (b'Show', 0x00, 0xF50F), (b'Wait', 4, 0x1F9A),
        (b'LoginButton_Click', 4, 0x0C1A),
        (b'Hide', 0x00, 0x7A39),
        (b'Workbook', 4, 0x186B),
        (b'iTestableProject', 0x80, 0x3408, 0x00, -253),
        (b'TestRunner', 0x80, 0xF9E0, 0x00, -253),
        (b'CreateTestRunner', 0x80, 0x0707, 0x00, -253),
        (b'iTestCase', 0x80, 0xE037, 0x00, -253),
        (b'Class', 4, 0xBB1A),
        (b'Initialize', 0x80, 0x4ED3, 0x00, 0x103),
        (b'CreateTestCase', 0x80, 0xD159, 0x00, -253),
        (b'Actual', 0x80, 0x9101, 0x00, -253),
        (b'Expected', 0x80, 0xA87F, 0x00, -253),
        (b'AssertEquals', 0x80, 0x45C1, 0x00, -253),
        (b'_B_var_iLength', 0x80, 0xE3C2, 0x00, -253),
        (b'_B_var_Left', 0x00, 0xE151), (b'Item', 0x00, 0x7AD7),
        (b'AssertObjectStringEquals', 0x80, 0xF2A4, 0x00, 0x00),
        (b'Result', 0x80, 0x7275, 0x00, 0x00),
        (b'TestReporter', 0x80, 0xDE8F, 0x00, 0x00),
        (b'_B_var_if', 0x80, 0xF250, 0x00, 0x00),
        (b'push', 0x00, 0xEA01),
        (b'_B_var_push', 0x80, 0x4F2E, 0x00, 0x00),
        (b'ArrayPush', 0xAC, 0xA01B, 0x00, 0x00),
        (b'newValue', 4, 0x7FA2), (b'ArrayOush', 0x00, 0xDA7D),
        (b'_B_var_ArrayOush', 0x80, 0xD441, 0x00, 0x00),
        (b'ArrayPushaJoin', 0x00, 0x3095),
        (b'_B_var_ArrLen', 0x80, 0xDD6F, 0x00, 0x00),
        (b'IsEmpty', 0x00, 0xF90A)
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

    ca = cache._post_module_section()
    file_data = f.read(0x14e)
    f.seek(0x2f800)
    file_data += f.read(len(ca) - len(file_data))
    assert ca == file_data

    ca = cache._identifier_section()
    file_data = f.read(0x52c)
    f.seek(0x31200)
    file_data += f.read(len(ca) - len(file_data))
    assert ca == file_data

    # full _vba_project is 2c2b bytes

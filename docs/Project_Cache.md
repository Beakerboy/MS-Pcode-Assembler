# Project Cache
The _VBA_PEOJECT stream contains a performance cache that begins 7 bytes after the beginning, and fills the remainder of the stream.
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="1">SignatureByte</td>
    <td class="tg-0pky" colspan="15">Header</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
   <tr>
    <td class="tg-0pky" colspan="16">Libraries</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Class/User Forms</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Compile-Time Parameters</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Type Info</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Project Description</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Help File</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Data (0x64 bytes)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Modules</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Identifiers</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>SignatureByte (1 byte):</b> Specifies the beginning of the PerformanceCache. MUST be 0xFF.

## Header

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="4">0x409</td>
    <td class="tg-0pky" colspan="4">0x409</td>
    <td class="tg-0pky" colspan="2">Version</td>
    <td class="tg-0pky" colspan="2">Data0</td>
    <td class="tg-0pky" colspan="4">0</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">Data1</td>
  </tr>
</tbody>
</table>

    Example Data:
    09 04 00 00 09 04 00 00 E4 04 03 00 00 00 00 00  .........ä.......
    00 00 00 00 01 00                                ..........
    
## Libraries

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="2">Count</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="12">Records</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

### Library Record
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="16">Lib or Project (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">...</td>
    <td class="tg-0pky" colspan="10">Data</td>
    <td class="tg-0pky" colspan="2">Struct</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Struct Object (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>Lib or Project (2 bytes):</b> A Library Ref is a two byte size/data field, while a project reference is a two byte size/data field followed by a second two byte size/data field.

<b>Struct (2 bytes):</b> If this is zero, the following data structure is omitted.

    Example Data:
          20 01 2A 00 5C 00 47 00 7B 00 30 00 30 00      *.\.G.{.0.0.
    30 00 32 00 30 00 34 00 45 00 46 00 2D 00 30 00  0.2.0.4.E.F.-.0.
    30 00 30 00 30 00 2D 00 30 00 30 00 30 00 30 00  0.0.0.-.0.0.0.0.
    2D 00 43 00 30 00 30 00 30 00 2D 00 30 00 30 00  -.C.0.0.0.-.0.0.
    30 00 30 00 30 00 30 00 30 00 30 00 30 00 30 00  0.0.0.0.0.0.0.0.
    34 00 36 00 7D 00 23 00 34 00 2E 00 32 00 23 00  4.6.}.#.4...2.#.
    39 00 23 00 43 00 3A 00 5C 00 50 00 72 00 6F 00  9.#.C.:.\.P.r.o.
    67 00 72 00 61 00 6D 00 20 00 46 00 69 00 6C 00  g.r.a.m. .F.i.l.
    65 00 73 00 5C 00 43 00 6F 00 6D 00 6D 00 6F 00  e.s.\.C.o.m.m.o.
    6E 00 20 00 46 00 69 00 6C 00 65 00 73 00 5C 00  n. .F.i.l.e.s.\.
    4D 00 69 00 63 00 72 00 6F 00 73 00 6F 00 66 00  M.i.c.r.o.s.o.f.
    74 00 20 00 53 00 68 00 61 00 72 00 65 00 64 00  t. .S.h.a.r.e.d.
    5C 00 56 00 42 00 41 00 5C 00 56 00 42 00 41 00  \.V.B.A.\.V.B.A.
    37 00 2E 00 31 00 5C 00 56 00 42 00 45 00 37 00  7...1.\.V.B.E.7.
    2E 00 44 00 4C 00 4C 00 23 00 56 00 69 00 73 00  ..D.L.L.#.V.i.s.
    75 00 61 00 6C 00 20 00 42 00 61 00 73 00 69 00  u.a.l. .B.a.s.i.
    63 00 20 00 46 00 6F 00 72 00 20 00 41 00 70 00  c. .F.o.r. .A.p.
    70 00 6C 00 69 00 63 00 61 00 74 00 69 00 6F 00  p.l.i.c.a.t.i.o.
    6E 00 73 00 00 00 00 00 00 00 00 00 00 00 00 00  n.s.............

    Example Data:
                      84 00 2A 00 5C 00 43 00 43 00        ?.*.\.C.C.
    3A 00 5C 00 55 00 73 00 65 00 72 00 73 00 5C 00  :.\.U.s.e.r.s.\.
    6B 00 6E 00 6F 00 77 00 61 00 63 00 7A 00 79 00  k.n.o.w.a.c.z.y.
    6B 00 5C 00 41 00 70 00 70 00 44 00 61 00 74 00  k.\.A.p.p.D.a.t.
    61 00 5C 00 52 00 6F 00 61 00 6D 00 69 00 6E 00  a.\.R.o.a.m.i.n.
    67 00 5C 00 4D 00 69 00 63 00 72 00 6F 00 73 00  g.\.M.i.c.r.o.s.
    6F 00 66 00 74 00 5C 00 41 00 64 00 64 00 49 00  o.f.t.\.A.d.d.I.
    6E 00 73 00 5C 00 53 00 51 00 4C 00 6C 00 69 00  n.s.\.S.Q.L.l.i.
    62 00 2E 00 78 00 6C 00 61 00 6D 00 6A 00 2A 00  b...x.l.a.m.j.*.
    5C 00 43 00 2E 00 2E 00 5C 00 2E 00 2E 00 5C 00  \.C.....\.....\.
    41 00 70 00 70 00 44 00 61 00 74 00 61 00 5C 00  A.p.p.D.a.t.a.\.
    52 00 6F 00 61 00 6D 00 69 00 6E 00 67 00 5C 00  R.o.a.m.i.n.g.\.
    4D 00 69 00 63 00 72 00 6F 00 73 00 6F 00 66 00  M.i.c.r.o.s.o.f.
    74 00 5C 00 41 00 64 00 64 00 49 00 6E 00 73 00  t.\.A.d.d.I.n.s.
    5C 00 53 00 51 00 4C 00 6C 00 69 00 62 00 2E 00  \.S.Q.L.l.i.b...
    78 00 6C 00 61 00 6D 00 DE 42 D9 5D 0A 00 00 00  x.l.a.m._BU]....
    00 00 00 00                                      ....

#### Data Structure

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="2">Size</td>
    <td class="tg-0pky" colspan="14">Data(varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">wLength</td>
    <td class="tg-0pky" colspan="2">Data (optional)</td>
    <td class="tg-0pky" colspan="12">Data(varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="14">...</td>
  </tr>
</tbody>
</table>

<b>wLength (2 bytes):</b> the following 2 bytes of data os omitted if wLength is zero.

<b>Data (2 bytes):</b> 

<b>Data (varies):</b> a data steam the size specified by wLength.

<b>Data (30 bytes):</b>

## User Class
A list of two byte data.

    Example Data:
    09 00 02 00 02 00 02 00 02 00 02 00 02 00 01 00  ....................
    01 00 02 04                                      ....

## Compile Time Data
A list of four byte data. followed by 2 mystery bytes.

    Example Data:
    06 00 0C 02 00 00 0E 02 01 00 10 02 00 00 12 02  ................
    00 00 14 02 01 00 16 02 01 00 6E 03              ..........n.

## Data
A large block of data. The last two bytes are the project cookie.

    Example Data:
                                  00 00 00 00 FF FF           .......
    00 00 4F 58 D9 5D 0D 00 FF FF FF FF 00 00 FF FF  ..OXU]..........
    FF FF 01 00 FF FF FF FF 02 00 04 00 FF FF FF FF  ................
    08 00 03 00 05 00 07 00 06 00 FF FF FF FF FF FF  ................
    FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  ................
    FF FF FF FF FF FF FF FF 01 00 00 00 00 00 00 00  ................
    00 00 00 00 00 00 00 00 00 00 00 00 40 BA        ............@º

## Modules
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="2">Count</td>
    <td class="tg-0pky" colspan="14">Module Records</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

### Module Record
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="2">Size</td>
    <td class="tg-0pky" colspan="14">Name (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">Size (0x14)</td>
    <td class="tg-0pky" colspan="14">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="6">...</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="2">Size</td>
    <td class="tg-0pky" colspan="4">Name</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="6">...</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">Cookie</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">Count</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="8">Records</td>
    <td class="tg-0pky" colspan="1">Data</td>
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="3">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="1">...</td>
    <td class="tg-0pky" colspan="2">-1 or 0</td>
  </tr>
</tbody>
</table>

<b>Records (8 bytes each):</b> 4 bytes of data and 4 bytes of -1.

    Example Data:
                            18 00 54 00 68 00 69 00          ..T.h.i.
    73 00 57 00 6F 00 72 00 6B 00 62 00 6F 00 6F 00  s.W.o.r.k.b.o.o.
    6B 00 14 00 30 00 5B 00 36 00 33 00 63 00 34 00  k...0.[.6.3.c.4.
    31 00 61 00 31 00 31 00 FF FF 2B 02 18 00 54 00  1.a.1.1...+...T.
    68 00 69 00 73 00 57 00 6F 00 72 00 6B 00 62 00  h.i.s.W.o.r.k.b.
    6F 00 6F 00 6B 00 FF FF 72 C4 00 00 00 00 00 00  o.o.k...rÄ......
    00 02 00 00 00 3B 03 00 00 FF FF                 .....;.....

## Identifiers
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="6">Data</td>
    <td class="tg-0pky" colspan="4">Size</td>
    <td class="tg-0pky" colspan="6">Data (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">...</td>
    <td class="tg-0pky" colspan="6">Data</td>
    <td class="tg-0pky" colspan="2">W0</td>
    <td class="tg-0pky" colspan="2">NumIds</td>
    <td class="tg-0pky" colspan="2">W1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Identifier Records</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

### Identifier Record
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky">00</th>
    <th class="tg-0pky">01</th>
    <th class="tg-0pky">02</th>
    <th class="tg-0pky">03</th>
    <th class="tg-0pky">04</th>
    <th class="tg-0pky">05</th>
    <th class="tg-0pky">06</th>
    <th class="tg-0pky">07</th>
    <th class="tg-0pky">08</th>
    <th class="tg-0pky">09</th>
    <th class="tg-0pky">0A</th>
    <th class="tg-0pky">0B</th>
    <th class="tg-0pky">0C</th>
    <th class="tg-0pky">0D</th>
    <th class="tg-0pky">0E</th>
    <th class="tg-0pky">0F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="2">T/L</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="2">T/L</td>
    <td class="tg-0pky" colspan="6">Data (optional)</td>
    <td class="tg-0pky" colspan="4">Name (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="12">...</td>
    <td class="tg-0pky" colspan="4">Data (optional)</td>
  </tr>
</tbody>
</table>

<b>T/L (2 bytes):</b> Type / Length. If this is 0x0000 then the next two byes and following T/L will be present. Otherwise the length and type of the identifier name.

<b>Data (2 bytes):</b> Optional. Only present if the first T/L is 0x0000.

<b>T/L (2 bytes):</b> Optional. The length and type of the identifier name.

<b>Data (6 bytes):</b> Optional. This data is absent if the Type is less than 0x80.

<b>Name (varies):</b> The identifier name.

<b>Data (4 bytes):</b> Optional. This data is absent if the first T/L is 0x0000.

    Example Data:
    00 00 9B 00 05 80 14 00 FF 03 05 00 52 65 44 69  ..?..?......ReDi
    6D                                               m

    Example Data:
    09 80 00 00 FF 03 01 00 5F 45 76 61 6C 75 61 74 .?......_Evaluat
    65 18 D9 10 00                                  e.U..

    Example Data:
    03 04 4D 61 63 B3 B2 10 00                      ..Mac3²..

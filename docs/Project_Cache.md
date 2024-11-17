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
    <td class="tg-0pky" colspan="16">Modules</td>
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
    <td class="tg-0pky" colspan="2">0x4E4</td>
    <td class="tg-0pky" colspan="2">Data0</td>
    <td class="tg-0pky" colspan="4">0</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">Data1</td>
    <td class="tg-0pky" colspan="2">Data2</td>
    <td class="tg-0pky" colspan="2">Data3</td>
  </tr>
</tbody>
</table>

<b>Data1 (2 byte):</b> Data1 plus Data2 seem to sum to the number of library records.

    Example Data:
    09 04 00 00 09 04 00 00 E4 04 03 00 00 00 00 00  .........ä.......
    00 00 00 00 01 00 07 00 02 00                    ..........
    
## Libraries
Immediately following the header is a series of size/data/zero blocks. there are LibIDRecord and ProjectReference structures.

### Library Record
Is there something that indicates how many library record are in the stream?
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
    <td class="tg-0pky" colspan="14">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">...</td>
    <td class="tg-0pky" colspan="12">0</td>
  </tr>
</tbody>
</table>

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

# Data
## Modules
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
    <td class="tg-0pky" colspan="2">Name</td>
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
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="2">-1</td>
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

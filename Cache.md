# Performance Cache
The performance cache precedes the compressed source container within a vbaProject.bin Module Stream.
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
    <td class="tg-0pky" colspan="16">DeclarationTable</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">GUIDs</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">454D Section</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>0xFF
  <tr>
    <td class="tg-0pky" colspan="16">128 bytes of 0xFF</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">ObjectTable</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">UTF-16 GUID</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">IndirectTable</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Lots of F's</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Rffff Section</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">DF Section</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">58 bytes of zeroes</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">Pcode</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>
<b>SignatureByte (1 byte):</b> Specifies the beginning of the PerformanceCache. MUST be 0x01.

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
    <td class="tg-0pky" colspan="4">Header</td>
    <td class="tg-0pky" colspan="4">DF offset</td>
    <td class="tg-0pky" colspan="4">RFFFF Offset</td>
    <td class="tg-0pky" colspan="4">45 Offset</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">IndirectTableOffset</td>
    <td class="tg-0pky" colspan="4">? Offset 3</td>
    <td class="tg-0pky" colspan="4">PcodeDirectoryOffset</td>
    <td class="tg-0pky" colspan="4">End Offset</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">Data1</td>
    <td class="tg-0pky" colspan="4">1</td>
    <td class="tg-0pky" colspan="2">ProjectCookie</td>
    <td class="tg-0pky" colspan="2">ModuleCookie</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="2">0xB6</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
  </tr>
</tbody>
</table>

<b>Header (4 bytes):</b> Final byte MUST be 0x16. The second to the last byte is the same on every module stream within a particular file. Should this be split into one byte, two bytes and one byte?

<b>ObjectTableOffset (4 bytes):</b> Offset to the 0xDF that follows the 45 Section</a>.

<b>RFFFF Offset (4 bytes):</b > Offset to the RFFFFs

<b>45 Offset (4 bytes):</b > The offset to 0x454D.

<b>IndirectTableOffset (4 bytes):</b> 10 less than the offset to the <a href="#indirect-table"><b>IndirectTable</b></a>.

<b>? Offset3 (4 bytes):</b > If there is no RFFF data, then -1, otherwise it's the offset one after the DF othat starts the DF Section.

<b>PcodeDirectoryOffset (4 bytes):</b> 60 less than the offset to the <a href="pcode"><b>Pcode</b></a>.

<b>End Offset (4 bytes):</b> Marks the end of the Pcode data. The compressed source container is 6 bytes after this.

<b>Data1 (4 bytes):</b>

<b>ProjectCookie (2 bytes):</b> The value from the Project stream.

<b>ModuleCookie (2 bytes):</b> The value from the Project stream.

<b>Data2 (4 bytes):</b>

<b>Data3 (4 bytes):</b>

    Example Data:
    16 03 00 01 F0 00 00 00 DA 02 00 00 D4 00 00 00  ....d...U...O...
    00 02 00 00 FF FF FF FF E1 02 00 00 35 03 00 00  ........á...5...
    00 00 00 00 01 00 00 00 B9 78 72 C4 00 00 FF FF  ........1xrÄ....
    23 00 00 00 88 00 00 00 B6 00 FF FF 01 01        #...?...¶.....

## Declaration Table
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
    <td class="tg-0pky" colspan="4">Size</td>
    <td class="tg-0pky" colspan="12">Data (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="4">0</td>
  </tr>
</tbody>
</table>
<b>DeclarationTableSize (4 bytes):</b> The value from the Project stream.

    Example Data:
    00 00 00 00 FF FF FF FF 00 00 00 00  ............

## Guids
Several Guids in binary form are packed together
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
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="8">Guid</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="8">...</td>
    <td class="tg-0pky" colspan="8">Guid</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="8">...</td>
    <td class="tg-0pky" colspan="8">Guid</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="8">...</td>
    <td class="tg-0pky" colspan="4">Count</td>
    <td class="tg-0pky" colspan="4">Guid (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="12">...</td>
    <td class="tg-0pky" colspan="4">16</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">3</td>
    <td class="tg-0pky" colspan="4">5</td>
    <td class="tg-0pky" colspan="4">7</td>
    <td class="tg-0pky" colspan="4">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
    <td class="tg-0pky" colspan="4">8</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0x78</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">...</td>
    <td class="tg-0pky" colspan="1">8</td>
    <td class="tg-0pky" colspan="13">Guid</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="3">...</td>
    <td class="tg-0pky" colspan="13">Guid</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="3">...</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="4">0</td>
  </tr>
</tbody>
</table>

    Example Data:
    FF FF 90 00 FF FF 00 00 5B F4 8B 2D 59 F3 79 41  ..?.....[ô?-YóyA
    BC 8C EA 13 9C 57 77 5F 2A 3D FB FC FA A0 68 10  ¼?ê.?Ww_*=ûüú h.
    A7 38 08 00 2B 33 71 B5 00 00 00 00 00 00 00 00  §8..+3qµ........
    00 00 00 00 00 00 00 00 01 00 00 00 3F 65 3E ED  ............?e>í
    E0 D3 F8 41 89 D4 7A 21 2D 16 D1 12 10 00 00 00  àOoA?Oz!-.Ñ.....
    03 00 00 00 05 00 00 00 07 00 00 00 FF FF FF FF  ................
    FF FF FF FF 01 01 08 00 00 00 FF FF FF FF 78 00  ..............x.
    00 00 08 3F 65 3E ED E0 D3 F8 41 89 D4 7A 21 2D  ...?e>íàOoA?Oz!-
    16 D1 12 5B F4 8B 2D 59 F3 79 41 BC 8C EA 13 9C  .Ñ.[ô?-YóyA¼?ê.?
    57 77 5F FF FF 00 00 00 00                       Ww_.......

## 454D Section
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
    <td class="tg-0pky" colspan="4">SignatureBytes</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">0xDF</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">Data</td>
  </tr>
</tbody>
</table>
<b>SignatureBytes (2 bytes):</b> Specifies the beginning of the section. MUST be 0x454D.

This structure ends with 64 0xFFFF.

## Object Table
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
    <td class="tg-0pky" colspan="4">Length</td>
    <td class="tg-0pky" colspan="12">Data (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
    <td class="tg-0pky" colspan="4">0</td>
  </tr>
</tbody>
</table>

<b>Length (4 byte):</b> The number of bytes of data.

<b>Object Table Entries (10 bytes each):</b> 

#### Object Table Entry
Each <b>Object Table Entry</b> is 10 bytes in length
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
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0</td>
  </tr>
</tbody>
</table>

    Example Data:
    02 00 53 4C FF FF FF FF 00 00  ..SL......

## UTF-16 Guid
If the module has a GUID, its UTF-16 representation, with brackets and a leading "0" character, is included in the cache.

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
    <td class="tg-0pky" colspan="14">UTF16GuidRecord (optional)(varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">varies</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
  </tr>
</tbody>
</table>
<b>Count (2 bytes):</b> The number of guids. If the count is zero, the record it omitted.

<b>UTF16GuidRecord ():</b> A <b>UTF16GuidRecord</b>.

### UTF-16 GUID record
A standard size/data record. There may be multiple guids. Identical to the module VB_BASE attribute.
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
    <td class="tg-0pky" colspan="2">Length</td>
    <td class="tg-0pky" colspan="14">GUIDs</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

    Example Data:
    4E 00 30 00 7B 00 30 00 30 00 30 00 32 00 30 00  N.0.{.0.0.0.2.0.
    38 00 31 00 39 00 2D 00 30 00 30 00 30 00 30 00  8.1.9.-.0.0.0.0.
    2D 00 30 00 30 00 30 00 30 00 2D 00 43 00 30 00  -.0.0.0.0.-.C.0.
    30 00 30 00 2D 00 30 00 30 00 30 00 30 00 30 00  0.0.-.0.0.0.0.0.
    30 00 30 00 30 00 30 00 30 00 34 00 36 00 7D 00  0.0.0.0.0.4.6.}.

## Indirect Table
A collection of two or two and four byte data values.
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
    <td class="tg-0pky" colspan="4">Length</td>
    <td class="tg-0pky" colspan="12">Data (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>Length (4 byte):</b> The number of bytes of data.

    Example Data:
    
## F Section
This is a 130 byte bock which is mostly -1 data elements. The four bytes at offset 0x1C matches the value at 0x34.

    Example Data:
    00 00 FF FF 00 00 01 00 00 00 00 00 00 00 00 00  ................
    FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00  ................
    FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF  ................
    FF FF FF FF 00 00 00 00 FF FF FF FF FF FF FF FF  ................
    FF FF FF FF FF FF FF FF FF FF FF FF 00 00 00 00  ................
    00 00 00 00 FF FF 00 00 FF FF FF FF FF FF 00 00  ................
    00 00 FF FF FF FF FF FF FF FF FF FF FF FF FF FF  ................
    FF FF FF FF FF FF FF FF FF FF 00 00 FF FF FF FF  ................
    FF FF  ..
    
## RFFFF Section
A collection of Rfff records...whatever they are. Are there bytes that indicate how many records there are besides the RFFF offset?

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
    <td class="tg-0pky" colspan="5">Data</td>
    <td class="tg-0pky" colspan="1">0</td>
    <td class="tg-0pky" colspan="10">RFFFFs (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>
<b> RFFFFs :</b> one or more RFFFF records

    Example Data:
    73 62 C6 63 07 00  sbÆc..

### RFFFF Record
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
    <td class="tg-0pky" colspan="1">1</td>
    <td class="tg-0pky" colspan="2">size</td>
    <td class="tg-0pky" colspan="10">data</td>
  </tr>
</tbody>
</table>

    Example Data:
    01 24 00 2A 00 5C 00 52 00 66 00 66 00 66 00 66  .$.*.\.R.f.f.f.f
    00 2A 00 32 00 33 00 36 00 33 00 63 00 36 00 39  .*.2.3.6.3.c.6.9
    00 61 00 37 00 34 00                             .a.7.4.

## DF Section
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
    <td class="tg-0pky" colspan="1">0xDF</td>
    <td class="tg-0pky" colspan="2">Count</td>
    <td class="tg-0pky" colspan="13">Data (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

    Example Data:
    DF 01 00 00 00 00 00 FF FF FF FF 78 00 00 00 06  ß..........x....
    00 10 00                                         ...

### DF Data
If there is data, we start with "00 00 00 00", then follow with a sequence of DF records.
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
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="12">DF Records (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>DF Records (12 bytes each):</b>

#### DF Record
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
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="4">Data</td>
    <td class="tg-0pky" colspan="2">Data</td>
    <td class="tg-0pky" colspan="2">Data</td>
  </tr>
</tbody>
</table>

After this is 58 0's...Sometimes 56 zeroes?
## Pcode

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
    <td class="tg-0pky" colspan="2">SignatureBytes</td>
    <td class="tg-0pky" colspan="14">PcodeDirectory (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">PcodeTable (varies)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>SignatureBytes (2 byte):</b> Specifies the beginning of the Pcode. MUST be 0xCAFE.

<b>PcodeDirectory (varies):</b> An array of PcodeDirectory objects.

<b>PcodeTable (varies):</b> The Pcode.

### Pcode Directory
The <b>Pcode Directory</b> is a list of one <b>PcodeDirectoryRecord</b> for each line in the module source file.
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
    <td class="tg-0pky" colspan="2">SignatureBytes</td>
    <td class="tg-0pky" colspan="2">Length</td>
    <td class="tg-0pky" colspan="12">PcodeDirectoryRecord</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
  </tr>
</tbody>
</table>

<b>SignatureBytes (2 bytes):</b> Specifies the beginning of the PcodeDirctory. MUST be 0x0001.

<b>Length (2 bytes):</b> Specifies the number of PcodeDirectoryRecord listings. MUST be equal to the number of lines in the source file.

<b>PcodeDirectoryRecords (12 bytes each):</b>

#### Pcode Directory Record
Each <b>Pcode Directory Record</b> Points to the location in the <b>Pcode Table</b> that holds the opcodes for the particular line in the source code.
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
    <td class="tg-0pky" colspan="4">????</td>
    <td class="tg-0pky" colspan="2">Length</td>
    <td class="tg-0pky" colspan="2">????</td>
    <td class="tg-0pky" colspan="4">Offset</td>
  </tr>
</tbody>
</table>

    Example Data:
    00 80 09 00 00 00 00 00 FF FF FF FF  .?..........
    42 A1 08 00 06 00 0C 00 10 00 00 00  B¡..........

### Pcode Data
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
    <td class="tg-0pky" colspan="4">Size</td>
    <td class="tg-0pky" colspan="12">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0</td>
  </tr>
</tbody>
</table>
Insert format of data. Each data element is padded to fill 8 byte increments.


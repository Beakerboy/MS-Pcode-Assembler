# MS-Pcode-Assembler
Create the VBA performance cache from source code.

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
    <td class="tg-0pky" colspan="16">GUIDs</td>
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
    <td class="tg-0pky" colspan="16">Mystery</td>
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
    <td class="tg-0pky" colspan="4">ObjectTableOffset</td>
    <td class="tg-0pky" colspan="4"> ? Offset</td>
    <td class="tg-0pky" colspan="4">0xD4</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">IndirectTableOffset</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="4">PcodeDirectoryOffset</td>
    <td class="tg-0pky" colspan="4">????</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="4">1</td>
    <td class="tg-0pky" colspan="2">ProjectCookie</td>
    <td class="tg-0pky" colspan="2">ModuleCookie</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">???</td>
    <td class="tg-0pky" colspan="4">???</td>
    <td class="tg-0pky" colspan="2">0xB6</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
    <td class="tg-0pky" colspan="2">0</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="2">...</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
</tbody>
</table>

<b>Header (4 bytes):</b> Final byte MUST be 0x16. The second to the last byte is the same on every module stream within a particular file.

<b>ObjectTableOffset (4 bytes):</b> 138 less than the offset to the <a href="#object-table"><b>ObjectTable</b></a>.

<b>? Offset (4 bytes):</b > An offset to an unknown record type.

<b>IndirectTableOffset (4 bytes):</b> 10 less than the offset to the <a href="#indirect-table"><b>IndirectTable</b></a>.

<b>-1 (4 bytes):</b>All Fs.

<b>PcodeDirectoryOffset (4 bytes):</b> 60 less than the offset to the <a href="pcode"><b>Pcode</b></a>.

<b>ProjectCookie (2 bytes):</b> The value from the Project stream.

<b>ModuleCookie (2 bytes):</b> The value from the Project stream.

## Guids
Guids in binary form are packed together
The data is then padded with FF to offset 0x179.

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

## UTF-16 Guid
If the module has a GUID, it's UTF-16 representation, with brackets and a leading "0" character, is included in the cache.

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
    <td class="tg-0pky" colspan="2">1 or 0</td>
    <td class="tg-0pky" colspan="14">UTF16GuidRecord (optional)</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
  </tr>
</tbody>
</table>
<b>1 or 0 (2 bytes):</b> 1 if the guid is included, 0 if not.

<b>UTF16GuidRecord (80 bytes):</b> A <b>UTF16GuidRecord</b>.

### UTF-16 GUID record
A standard size/data record
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
    <td class="tg-0pky" colspan="2">Length (0x4E)</td>
    <td class="tg-0pky" colspan="14">GUID</td>
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
    <td class="tg-0pky" colspan="16">PcodeTable (varies)</td>
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
    <td class="tg-0pky" colspan="4">????</td>
  </tr>
</tbody>
</table>

<b>SignatureBytes (2 byte):</b> Specifies the beginning of the PcodeDirctory. MUST be 0x0001.

<b>Length (2 byte):</b> Specifies the number of PcodeDirectoryRecord listings. MUST be equal to the number of lines in the source file.

<b>PcodeDirectoryRecord (12 byte):</b>

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

### Pcode Data
Next the line data, are they padded? For example, 6 data bytes followed with 0x0000 and 2 bytes followed by 0xFFFF and 4 mystery bytes.


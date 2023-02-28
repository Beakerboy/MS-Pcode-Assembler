# MS-Pcode-Assembler
Create the VBA performance cache from source code.

The performance cache precedes the compressed source container within a vbaProject.bin Module Stream.

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
    <td class="tg-0pky" colspan="1">SignatureByte</td>
    <td class="tg-0pky" colspan="4">Header</td>
    <td class="tg-0pky" colspan="4">ObjectTableOffset</td>
    <td class="tg-0pky" colspan="4"> ? Offset</td>
    <td class="tg-0pky" colspan="3">D4</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="1">...</td>
    <td class="tg-0pky" colspan="4">IndirectTableOffset</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="4">PcodeDirectoryOffset</td>
    <td class="tg-0pky" colspan="3">????</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="1">...</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="4">1</td>
    <td class="tg-0pky" colspan="2">ProjectCookie</td>
    <td class="tg-0pky" colspan="2">ModuleCookie</td>
    <td class="tg-0pky" colspan="2">0</td>
    <td class="tg-0pky" colspan="1">-1</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="1">...</td>
    <td class="tg-0pky" colspan="4">???</td>
    <td class="tg-0pky" colspan="4">???</td>
    <td class="tg-0pky" colspan="2">0xB6</td>
    <td class="tg-0pky" colspan="2">-1</td>
    <td class="tg-0pky" colspan="2">0x0101</td>
    <td class="tg-0pky" colspan="1">0</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="3">...</td>
    <td class="tg-0pky" colspan="4">-1</td>
    <td class="tg-0pky" colspan="4">0</td>
    <td class="tg-0pky" colspan="2">-1</td>
  </tr>
</tbody>
</table>

<b>SignatureByte (1 byte):</b> Specifies the beginning of the PerformanceCache. MUST be 0x01.

<b>Header (4 bytes):</b> Final byte MUST be 0x16. The second to the last byte is the same on every module stream within a particular file.

<b>ObjectTableOffset (4 bytes):</b> 138 less than the offset to the <a href="#object-table"><b>ObjectTable</b></a>.

<b>? Offset (4 bytes):</b >A mystery offset.

<b>D4 (4 bytes):</b> Value is 0xD4.

<b>IndirectTableOffset (4 bytes):</b> 10 less than the offset to the <a href="#indirect-table"><b>IndirectTable</b></a>.

<b>-1 (4 bytes):</b>All Fs.

<b>PcodeDirectoryOffset (4 bytes):</b> 60 less than the offset to the <a href="pcode"><b>Pcode</b></a>.

<b>ProjectCookie (2 bytes):</b> The value from the Project stream.

<b>ModuleCookie (2 bytes):</b> The value from the Project stream.

## Object Table

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


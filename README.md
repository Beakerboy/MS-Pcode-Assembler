# MS-Pcode-Assembler
Create the VBA performance cache from source code.

The performance cache precedes the compressed source container within a vbaProject.bin Module Stream.

# Header

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
    <th class="tg-0pky">10</th>
    <th class="tg-0pky">11</th>
    <th class="tg-0pky">12</th>
    <th class="tg-0pky">13</th>
    <th class="tg-0pky">14</th>
    <th class="tg-0pky">15</th>
    <th class="tg-0pky">16</th>
    <th class="tg-0pky">17</th>
    <th class="tg-0pky">18</th>
    <th class="tg-0pky">19</th>
    <th class="tg-0pky">1A</th>
    <th class="tg-0pky">1B</th>
    <th class="tg-0pky">1C</th>
    <th class="tg-0pky">1D</th>
    <th class="tg-0pky">1E</th>
    <th class="tg-0pky">1F</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky" colspan="1">SignatureByte</td>
    <td class="tg-0pky" colspan="4">Header</td>
    <td class="tg-0pky" colspan="4">ObjectTableOffset</td>
    <td class="tg-0pky" colspan="2">???</td>
  </tr>
</tbody>
</table>

<b>SignatureByte (1 byte):</b> Specifies the beginning of the PerformanceCache. MUST be 0x01.

<b>Header (4 bytes):</b>Final byte MUST be 0x16. The second to the last byte is the same on every module stream within a particular file.

<b>ObjectTableOffset (4 bytes):</b>138 less than the offset to the <b>ObjectTable</b>.


Magic code is 0xCAFE, followed by 0x0001. The next two bytes is the size of the following array.

Next is an array of 12 byte sequences. Each array element represents a line in the file. Bytes 4-5 are the length of the line, and 8-11 are the offset.

Next FF FF FF FF 01 01 XX XX XX XX

Next the line data, are they padded? For example, 6 data bytes followed with 0x0000 and 2 bytes followed by 0xFFFF and 4 mystery bytes.


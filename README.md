# MS-Pcode-Assembler
Create the VBA performance cache from source code.

The performance cache precedes the compressed source container within a vbaProject.bin Module Stream.

# Header

<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
    <th class="tg-0pky"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-0pky">00</td>
    <td class="tg-0pky">01</td>
    <td class="tg-0pky">02</td>
    <td class="tg-0pky">03</td>
    <td class="tg-0pky">04</td>
    <td class="tg-0pky">05</td>
    <td class="tg-0pky">06</td>
    <td class="tg-0pky">07</td>
    <td class="tg-0pky">08</td>
    <td class="tg-0pky">09</td>
    <td class="tg-0pky">0A</td>
    <td class="tg-0pky">0B</td>
    <td class="tg-0pky">0C</td>
    <td class="tg-0pky">0D</td>
    <td class="tg-0pky">0E</td>
    <td class="tg-0pky">0F</td>
    <td class="tg-0pky">10</td>
    <td class="tg-0pky">11</td>
    <td class="tg-0pky">12</td>
    <td class="tg-0pky">13</td>
    <td class="tg-0pky">14</td>
    <td class="tg-0pky">15</td>
    <td class="tg-0pky">16</td>
    <td class="tg-0pky">17</td>
    <td class="tg-0pky">18</td>
    <td class="tg-0pky">19</td>
    <td class="tg-0pky">1A</td>
    <td class="tg-0pky">1B</td>
    <td class="tg-0pky">1C</td>
    <td class="tg-0pky">1D</td>
    <td class="tg-0pky">1E</td>
    <td class="tg-0pky">1F</td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
  <tr>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
    <td class="tg-0pky"></td>
  </tr>
</tbody>
</table>

Like many containers, the cache begins with 0x01. The next byte is always 0x16 followed by a byte that is common among all streams in a file.

Magic code is 0xCAFE, followed by 0x0001. The next two bytes is the size of the following array.

Next is an array of 12 byte sequences. Each array element represents a line in the file. Bytes 4-5 are the length of the line, and 8-11 are the offset.

Next FF FF FF FF 01 01 XX XX XX XX

Next the line data, are they padded? For example, 6 data bytes followed with 0x0000 and 2 bytes followed by 0xFFFF and 4 mystery bytes.


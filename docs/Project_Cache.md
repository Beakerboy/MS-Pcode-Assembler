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
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
    <td class="tg-0pky" colspan="4"></td>
  </tr>
</tbody>
</table>



    Example Data:
    09 04 00 00 09 04 00 00 E4 04 03 00 00 00 00 00  .........ä.......
    00 00 00 00 01 00 07 00 02 00                    ..........


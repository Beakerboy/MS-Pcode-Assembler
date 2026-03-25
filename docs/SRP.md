# SRP
The SRP streams contains a performance cache information. How is each SRP stream tied to a specific module?
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
    <td class="tg-0pky" colspan="14">Data</td>
  </tr>
  <tr>
    <td class="tg-0pky" colspan="16">...</td>
  </tr>
</tbody>
</table>

<b>SignatureByte2 (2 byte):</b> Specifies the beginning of the SRP Stream. MUST be 0x5572.

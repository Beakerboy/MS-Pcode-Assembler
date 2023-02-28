# MS-Pcode-Assembler
Create the VBA performance cache from source code.

The performance cache precedes the compressed source container within a vbaProject.bin Module Stream.

# Header
Like many containers, the cache begins with 0x01. The next byte is always 0x16 followed by a byte that is common among all streams in a file.

Magic code is 0xCAFE, followed by 0x0001. The next two bytes is the size of the following array.

Next is an array of 12 byte sequences. Each array element represents a line in the file. Bytes 4-5 are the length of the line, and 8-11 are the offset.

Next FF FF FF FF 01 01 XX XX XX XX

Next the line data, are they padded? For example, 6 data bytes followed with 0x0000 and 2 bytes followed by 0xFFFF and 4 mystery bytes.


"""
#ip 4
seti 123 0 1        00  seti 123 _ b        b = 123
bani 1 456 1        01  bani b 456 b        b &= 456            # loop 4
eqri 1 72 1         02  eqri b 72 b           b = b == 72       # condition
addr 1 4 4          03  addr b ip ip            ip += b         # branch
seti 0 0 4          04  seti 0 _ ip         ip = 0              # continue 1
seti 0 3 1          05  seti 0 _ b          b = 0
bori 1 65536 5      06  bori b 65536 f      f = b | 65536       # loop 30
seti 8586263 3 1    07  seti 8586263 _ b      b = 8586263
bani 5 255 2        08  bani f 255 c          c = f & 255       # loop 27
addr 1 2 1          09  addr b c b              b += c
bani 1 16777215 1   10  bani b 16777215 b       b &= 16777215
muli 1 65899 1      11  muli b 65899 b          b *= 65899
bani 1 16777215 1   12  bani b 16777215 b       b &= 16777215
gtir 256 5 2        13  gtir 256 f c            c = 256 > f     # condition
addr 2 4 4          14  addr c ip ip              ip += c       # branch
addi 4 1 4          15  addi ip 1 ip              ip += 1       # break 17
seti 27 8 4         16  seti 27 _ ip              ip = 27       # break 28
seti 0 1 2          17  seti 0 _ c              c = 0
addi 2 1 3          18  addi c 1 d              d = c + 1       # loop 25
muli 3 256 3        19  muli d 256 d              d *= 256
gtrr 3 5 3          20  gtrr d f d                d = d > f     # condition
addr 3 4 4          21  addr d ip ip                ip += d     # branch
addi 4 1 4          22  addi ip 1 ip                ip += 1     # break 24
seti 25 8 4         23  seti 25 _ ip                ip = 25     # break 26
addi 2 1 2          24  addi c 1 c                c += 1
seti 17 7 4         25  seti 17 _ ip            ip = 17         # continue 18
setr 2 0 5          26  setr c _ f              f = c
seti 7 8 4          27  seti 7 _ ip           ip = 7            # continue 8
eqrr 1 0 2          28  eqrr b a c            c = b == a        # condition
addr 2 4 4          29  addr c ip ip            ip += c         # branch
seti 5 4 4          30  seti 5 _ ip         ip = 5              # continue 6
"""


def main():
    a = 5970144
    b = 0
    c = 0
    d = 0
    f = 0

    b = 123

    while True:
        b &= 456

        if b == 72:
            break

    b = 0

    while True:
        f = b | 65536
        b = 8586263

        while True:
            c = f & 255
            b += c
            b &= 16777215
            b *= 65899
            b &= 16777215

            if 256 > f:
                break

            c = 0

            while True:
                d = c + 1
                d *= 256

                if d > f:
                    break

                c += 1

            f = c

        print(b)

        if b == a:
            break


if __name__ == '__main__':
    main()

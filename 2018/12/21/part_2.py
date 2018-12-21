from sys import maxsize


"""
#ip 4
seti 123 0 1        00  seti 123 - b        b = 123
bani 1 456 1        01  bani b 456 b        b &= 456
eqri 1 72 1         02  eqri b 72 b         if b == 72:
addr 1 4 4          03  addr b ip ip            goto 5
seti 0 0 4          04  seti 0 - ip         goto 1
seti 0 3 1          05  seti 0 - b          b = 0
bori 1 65536 5      06  bori b 65536 f      f = b | 65536
seti 8586263 3 1    07  seti 8586263 - b    b = 8586263
bani 5 255 2        08  bani f 255 c        c = f & 255
addr 1 2 1          09  addr b c b          b += c
bani 1 16777215 1   10  bani b 16777215 b   b &= 16777215
muli 1 65899 1      11  muli b 65899 b      b *= 65899
bani 1 16777215 1   12  bani b 16777215 b   b &= 16777215
gtir 256 5 2        13  gtir 256 f c        if 256 > f:
addr 2 4 4          14  addr c ip ip            goto 16
addi 4 1 4          15  addi ip 1 ip        goto 17
seti 27 8 4         16  seti 27 - ip        goto 28
seti 0 1 2          17  seti 0 - c          c = 0
addi 2 1 3          18  addi c 1 d          d = c + 1
muli 3 256 3        19  muli d 256 d        d *= 256
gtrr 3 5 3          20  gtrr d f d          if d > f:
addr 3 4 4          21  addr d ip ip            goto 23
addi 4 1 4          22  addi ip 1 ip        goto 24
seti 25 8 4         23  seti 25 - ip        goto 26
addi 2 1 2          24  addi c 1 c          c += 1
seti 17 7 4         25  seti 17 - ip        goto 18
setr 2 0 5          26  setr c - f          f = c
seti 7 8 4          27  seti 7 - ip         goto 8
eqrr 1 0 2          28  eqrr b a c          if b == a:
addr 2 4 4          29  addr c ip ip            goto 31
seti 5 4 4          30  seti 5 - ip         goto 6
"""


def main():
    seen = set()
    last_b = 0

    a = 5970144
    b = 0
    c = 0
    d = 0
    f = 0

    while True:
        b = 123
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

            f //= 256

        if b in seen:
            break

        seen.add(b)
        last_b = b

    print(last_b)


if __name__ == '__main__':
    main()

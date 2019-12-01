def main():
    a = 0; b = 0; c = 0; d = 0; f = 0

    f += 2
    f *= f
    f *= 19
    f *= 11
    d += 4
    d *= 22
    d += 21
    f += d

    if a == 1:
        d = 27
        d *= 28
        d += 29
        d *= 30
        d *= 14
        d *= 32
        f += d
        a = 0

    b = 1

    while True:
        c = 1

        while True:
            d = b * c
            d = int(d == f)

            if d == 1:
                a += b

            c += 1
            d = int(c > f)

            if d == 1:
                break

        b += 1
        d = int(b > f)

        if d == 1:
            break

    print(a)


if __name__ == '__main__':
    main()

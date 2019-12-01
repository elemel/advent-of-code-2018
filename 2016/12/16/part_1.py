from sys import stdin


def main():
    initial_state = stdin.read().strip()
    a = list(initial_state)

    while len(a) < 272:
        b = list('1' if c == '0' else '0' for c in reversed(a))
        a.append('0')
        a.extend(b)

    a = a[:272]

    checksum = a

    while len(checksum) % 2 == 0:
        checksum = [
            '1' if a == b else '0'
            for a, b in zip(checksum[::2], checksum[1::2])
        ]

    print(''.join(checksum))


if __name__ == '__main__':
    main()

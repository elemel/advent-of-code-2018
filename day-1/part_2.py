import sys


def main():
    sequence = [int(line) for line in sys.stdin]
    current = 0
    seen = set([current])
    duplicate = None

    while not duplicate:
        for change in sequence:
            current += change

            if current in seen:
                duplicate = current
                break

            seen.add(current)

    print(duplicate)


if __name__ == '__main__':
    main()

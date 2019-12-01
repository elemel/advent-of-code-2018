from sys import stdin


def main():
    string_literals = [line.strip() for line in stdin]
    print(sum(2 + sum(c in '\\"' for c in l) for l in string_literals))


if __name__ == '__main__':
    main()

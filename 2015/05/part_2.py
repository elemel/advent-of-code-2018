from sys import stdin


def is_nice(s):
    return (
        any(s[i:i + 2] in s[i + 2:] for i in range(len(s) - 3)) and
        any(s[i] == s[i + 2] for i in range(len(s) - 2)))


def main():
    strings = [line.strip() for line in stdin]
    print(sum(is_nice(s) for s in strings))


if __name__ == '__main__':
    main()

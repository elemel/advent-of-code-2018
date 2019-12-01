from sys import stdin


def is_nice(s):
    return (
        sum(c in 'aeiou' for c in s) >= 3 and
        any(s[i] == s[i + 1] for i in range(len(s) - 1)) and
        all(s2 not in s for s2 in ['ab', 'cd', 'pq', 'xy']))


def main():
    strings = [line.strip() for line in stdin]
    print(sum(is_nice(s) for s in strings))


if __name__ == '__main__':
    main()

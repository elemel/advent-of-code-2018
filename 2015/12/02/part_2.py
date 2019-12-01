from sys import stdin


def parse_present(line):
    l, w, h = [int(s) for s in line.split('x')]
    return l, w, h


def wrap_present(present):
    s1, s2, _ = sorted(present)
    l, w, h = present
    return 2 * s1 + 2 * s2 + l * w * h


def main():
    presents = [parse_present(line.strip()) for line in stdin]
    print(sum(wrap_present(present) for present in presents))


if __name__ == '__main__':
    main()

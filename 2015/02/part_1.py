from sys import stdin


def parse_present(line):
    l, w, h = [int(s) for s in line.split('x')]
    return l, w, h


def wrap_present(present):
    l, w, h = present
    s1, s2, _ = sorted(present)
    return 2 * l * w + 2 * w * h + 2 * h * l + s1 * s2


def main():
    presents = [parse_present(line.strip()) for line in stdin]
    print(sum(wrap_present(present) for present in presents))


if __name__ == '__main__':
    main()

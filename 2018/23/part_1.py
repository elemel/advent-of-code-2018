from sys import stdin


def parse_nanobot(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    x, y, z, r = [int(s) for s in number_line.split()]
    return (x, y, z), r


def manhattan_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def main():
    nanobots = [parse_nanobot(line.strip()) for line in stdin]
    r1, p1 = max((r, p) for p, r in nanobots)

    print(sum(
        manhattan_distance(p1, p2) < r1
        for p2, _ in nanobots))


if __name__ == '__main__':
    main()

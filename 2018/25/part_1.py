from collections import defaultdict
from itertools import combinations
from sys import stdin


def parse_fixed_point(line):
    x, y, z, t = [int(s) for s in line.split(',')]
    return x, y, z, t


def manhattan_distance(p1, p2):
    return sum(abs(b - a) for a, b in zip(p1, p2))


def main():
    fixed_points = [parse_fixed_point(line.strip()) for line in stdin]
    neighbor_sets = defaultdict(set)

    for p1, p2 in combinations(fixed_points, 2):
        if manhattan_distance(p1, p2) <= 3:
            neighbor_sets[p1].add(p2)
            neighbor_sets[p2].add(p1)

    constellations = []
    closed = set()

    for p in fixed_points:
        if p in closed:
            continue

        open_ = [p]
        constellation = []

        while open_:
            p = open_.pop()

            if p in closed:
                continue

            closed.add(p)
            constellation.append(p)
            open_.extend(neighbor_sets[p])

        constellations.append(constellation)

    print(len(constellations))


if __name__ == '__main__':
    main()

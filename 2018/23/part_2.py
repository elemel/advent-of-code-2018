
from collections import defaultdict, deque
from sys import maxsize, stdin


def parse_nanobot(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    x, y, z, r = [int(s) for s in number_line.split()]
    p = x, y, z
    return p, r


def midpoint(p1, p2):
    return tuple((x1 + x2) // 2 for x1, x2 in zip(p1, p2))


def manhattan_distance(p1, p2):
    return sum(abs(x2 - x1) for x1, x2 in zip(p1, p2))


def in_range(c1, c2):
    p1, r1 = c1
    p2, r2 = c2
    return manhattan_distance(p1, p2) <= r1 + r2


def subdivide(p1, p2, p):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    x, y, z = p

    if x2 - x1 >= max(y2 - y1, z2 - z1):
        p3 = x, y2, z2
        p4 = x + 1, y1, z1
    elif y2 - y1 >= z2 - z1:
        p3 = x2, y, z2
        p4 = x1, y + 1, z1
    else:
        p3 = x2, y2, z
        p4 = x1, y1, z + 1

    return p3, p4


def main():
    nanobots = [parse_nanobot(line.strip()) for line in stdin]
    groups = defaultdict(set)

    for nanobot_1 in nanobots:
        for nanobot_2 in nanobots:
            if in_range(nanobot_1, nanobot_2):
                groups[nanobot_1].add((nanobot_2))

    group_stack = [(-len(group), nanobot) for nanobot, group in groups.items()]
    group_stack.sort()

    while group_stack:
        _, nanobot = group_stack.pop()
        group = groups.pop(nanobot)

        if len(group) > len(groups):
            break

        for nanobot_2 in group:
            if nanobot_2 != nanobot:
                groups[nanobot_2].remove(nanobot)

    x1 = max(x - r for (x, y, z), r in group)
    y1 = max(y - r for (x, y, z), r in group)
    z1 = max(z - r for (x, y, z), r in group)

    x2 = min(x + r for (x, y, z), r in group)
    y2 = min(y + r for (x, y, z), r in group)
    z2 = min(z + r for (x, y, z), r in group)

    p1 = x1, y1, z1
    p2 = x2, y2, z2

    region_queue = deque([(p1, p2)])
    min_distance = maxsize

    while region_queue:
        p1, p2 = region_queue.popleft()
        p = midpoint(p1, p2)
        r = max(manhattan_distance(p, p1), manhattan_distance(p, p2))
        c = p, r

        if not all(in_range(c, nanobot) for nanobot in group):
            continue

        if r == 0:
            distance = manhattan_distance((0, 0, 0), p)
            min_distance = min(min_distance, distance)
            continue

        p3, p4 = subdivide(p1, p2, p)
        region_queue.append((p1, p3))
        region_queue.append((p4, p2))

    print(min_distance)


if __name__ == '__main__':
    main()

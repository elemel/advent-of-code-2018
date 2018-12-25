
from collections import defaultdict, deque
from heapq import heappop, heappush
from sys import maxsize, stdin


def parse_nanobot(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    x, y, z, r = [int(s) for s in number_line.split()]
    return (x, y, z), r


def manhattan_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)


def in_range(c1, c2):
    p1, r1 = c1
    p2, r2 = c2
    return manhattan_distance(p1, p2) <= r1 + r2


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

        x1, y1, z1 = p1
        x2, y2, z2 = p2

        x = (x1 + x2) // 2
        y = (y1 + y2) // 2
        z = (z1 + z2) // 2

        p = x, y, z
        r = max(manhattan_distance(p, p1), manhattan_distance(p, p2))
        c = p, r

        if not all(in_range(c, nanobot) for nanobot in group):
            continue

        if r == 0:
            distance = manhattan_distance((0, 0, 0), p)
            min_distance = min(min_distance, distance)
            continue

        if x2 - x1 >= max(y2 - y1, z2 - z1):
            region_queue.append((p1, (x, y2, z2)))
            region_queue.append(((x + 1, y1, z1), p2))
        elif y2 - y1 >= z2 - z1:
            region_queue.append((p1, (x2, y, z2)))
            region_queue.append(((x1, y + 1, z1), p2))
        else:
            region_queue.append((p1, (x2, y2, z)))
            region_queue.append(((x1, y1, z + 1), p2))

    print(min_distance)


if __name__ == '__main__':
    main()

from collections import Counter, deque
from sys import stderr, stdin


def main():
    locations = [tuple(int(s) for s in line.split(',')) for line in stdin]

    x1 = min(x for (x, _) in locations)
    y1 = min(y for (_, y) in locations)
    x2 = max(x for (x, _) in locations)
    y2 = max(y for (_, y) in locations)

    inf = abs(x2 - x1) + abs(y2 - y1)
    grid = {}
    queue = deque((location, location, 0) for location in locations)
    hull = set()
    max_percentage = 0

    while queue:
        location, position, distance = queue.popleft()
        percentage = 100 * distance // inf

        if percentage > max_percentage:
            max_percentage = percentage
            print('Progress: %s%%' % percentage, file=stderr)

        if distance == inf:
            hull.add(location)
            continue

        old_location, old_distance = grid.get(position, (None, inf))

        if distance > old_distance:
            continue

        if distance == old_distance:
            if location != old_location:
                grid[position] = None, distance

            continue

        grid[position] = location, distance
        x, y = position
        queue.append((location, (x - 1, y), distance + 1))
        queue.append((location, (x + 1, y), distance + 1))
        queue.append((location, (x, y - 1), distance + 1))
        queue.append((location, (x, y + 1), distance + 1))

    sizes = Counter(
        location
        for _, (location, _) in grid.items()
        if location and location not in hull)

    _, size = sizes.most_common(1)[0]
    print(size)


if __name__ == '__main__':
    main()

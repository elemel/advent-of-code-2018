from collections import deque
from itertools import permutations
from sys import maxsize, stdin


def get_distances(map_, x, y):
    distances = {}
    queue = deque([(0, x, y)])
    visited = set()

    while queue:
        distance, x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if map_[y][x].isdigit():
            distances[int(map_[y][x])] = distance

        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            if map_[y + dy][x + dx] != '#':
                queue.append((distance + 1, x + dx, y + dy))

    return distances


def get_all_distances(map_, locations):
    all_distances = {}

    for i, (x, y) in locations.items():
        distances = get_distances(map_, x, y)

        for j, distance in distances.items():
            all_distances[i, j] = distance

    return all_distances


def get_total_distance(all_distances, path):
    total_distance = 0
    i = 0

    for j in path:
        total_distance += all_distances[i, j]
        i = j

    return total_distance


def main():
    map_ = [list(line.strip()) for line in stdin]

    locations = {
        int(c): (x, y)
        for y, row in enumerate(map_)
        for x, c in enumerate(row)
        if c.isdigit()
    }

    all_distances = get_all_distances(map_, locations)

    min_total_distance = min(
        get_total_distance(all_distances, path)
        for path in permutations(range(1, 8)))

    print(min_total_distance)


if __name__ == '__main__':
    main()

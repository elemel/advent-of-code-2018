from collections import deque
from sys import stdin


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def total_manhattan_distance(x, y, locations):
    return sum(manhattan_distance(x, y, x2, y2) for x2, y2 in locations)


def add_neighbors_to_queue(x, y, locations, queue):
    queue.append((x - 1, y, total_manhattan_distance(x - 1, y, locations)))
    queue.append((x + 1, y, total_manhattan_distance(x + 1, y, locations)))
    queue.append((x, y - 1, total_manhattan_distance(x, y - 1, locations)))
    queue.append((x, y + 1, total_manhattan_distance(x, y + 1, locations)))


def main():
    locations = [tuple(int(s) for s in line.split(',')) for line in stdin]

    x0 = sum(x for (x, _) in locations) // len(locations)
    y0 = sum(y for (_, y) in locations) // len(locations)

    queue = deque()
    queue.append((x0, y0, total_manhattan_distance(x0, y0, locations)))
    grid = {}

    while queue:
        x, y, distance = queue.popleft()

        if distance < grid.get((x, y), 10000):
            grid[x, y] = distance
            add_neighbors_to_queue(x, y, locations, queue)

    print(len(grid))


if __name__ == '__main__':
    main()

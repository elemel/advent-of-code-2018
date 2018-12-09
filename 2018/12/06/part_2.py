from sys import maxint, stdin


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    locations = [tuple(int(s) for s in line.split(',')) for line in stdin]

    min_x = min(x for x, _ in locations)
    min_y = min(y for _, y in locations)
    max_x = max(x for x, _ in locations)
    max_y = max(y for _, y in locations)

    print(sum(
        sum(manhattan_distance(x1, y1, x2, y2) for x2, y2 in locations) < 10000
        for x1 in range(min_x, max_x + 1)
        for y1 in range(min_y, max_y + 1)))


if __name__ == '__main__':
    main()

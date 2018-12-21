from collections import Counter
from sys import maxsize, stdin


def parse_location(line):
    x, y = [int(s) for s in line.split(',')]
    return x, y


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    locations = [parse_location(line.strip()) for line in stdin]

    min_x = min(x for x, _ in locations)
    min_y = min(y for _, y in locations)
    max_x = max(x for x, _ in locations)
    max_y = max(y for _, y in locations)

    area_sizes = Counter()
    infinite_areas = set()

    for y1 in range(min_y, max_y + 1):
        for x1 in range(min_x, max_x + 1):
            closest_locations = set()
            min_distance = maxsize

            for x2, y2 in locations:
                distance = manhattan_distance(x1, y1, x2, y2)

                if distance < min_distance:
                    closest_locations.clear()
                    min_distance = distance

                if distance == min_distance:
                    closest_locations.add((x2, y2))

            if len(closest_locations) == 1:
                [closest_location] = closest_locations
                area_sizes[closest_location] += 1

            if x1 in [min_x, max_x] or y1 in [min_y, max_y]:
                infinite_areas |= closest_locations

    for location in infinite_areas:
        area_sizes.pop(location, None)

    [(_, largest_area_size)] = area_sizes.most_common(1)
    print(largest_area_size)


if __name__ == '__main__':
    main()

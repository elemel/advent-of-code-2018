from sys import maxint, stdin


def manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def main():
    locations = [tuple(int(s) for s in line.split(',')) for line in stdin]

    min_x = min(x for x, _ in locations)
    min_y = min(y for _, y in locations)
    max_x = max(x for x, _ in locations)
    max_y = max(y for _, y in locations)

    sizes = len(locations) * [0]
    infinite = len(locations) * [False]

    for x1 in range(min_x, max_x + 1):
        for y1 in range(min_y, max_y + 1):
            closest_indices = []
            min_distance = maxint

            for i, (x2, y2) in enumerate(locations):
                distance = manhattan_distance(x1, y1, x2, y2)

                if distance < min_distance:
                    del closest_indices[:]
                    min_distance = distance

                if distance == min_distance:
                    closest_indices.append(i)

            if len(closest_indices) == 1:
                sizes[closest_indices[0]] += 1

            if x1 == min_x or x1 == max_x or y1 == min_y or y1 == max_y:
                for i in closest_indices:
                    infinite[i] = True

    print(max(size for i, size in enumerate(sizes) if not infinite[i]))


if __name__ == '__main__':
    main()

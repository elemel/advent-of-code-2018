from sys import maxsize, stdin


def parse_star(line):
    head, tail = line.split('<', 1)
    head, tail = tail.split('>', 1)
    x, y = [int(s) for s in head.split(',')]

    head, tail = tail.split('<', 1)
    head, tail = tail.split('>', 1)
    dx, dy = [int(s) for s in head.split(',')]

    return x, y, dx, dy


def get_bounds(stars, t):
    min_x = min(x + dx * t for x, _, dx, _ in stars)
    min_y = min(y + dy * t for _, y, _, dy in stars)
    max_x = max(x + dx * t for x, _, dx, _ in stars)
    max_y = max(y + dy * t for _, y, _, dy in stars)
    return min_x, min_y, max_x, max_y


def get_error(stars, t):
    min_x, min_y, max_x, max_y = get_bounds(stars, t)
    return (max_x - min_x) + (max_y - min_y)


def main():
    stars = [parse_star(line) for line in stdin]
    min_error = maxsize

    for t in range(0, maxsize):
        error = get_error(stars, t)

        if error > min_error:
            print(t - 1)
            return

        min_error = error


if __name__ == '__main__':
    main()

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


def get_fitness(stars, t):
    min_x, min_y, max_x, max_y = get_bounds(stars, t)
    return (max_x - min_x) * (max_y - min_y)


def print_message(stars, t):
    min_x, min_y, max_x, max_y = get_bounds(stars, t)

    grid = [
        ['.' for x in range(min_x, max_x + 1)]
        for y in range(min_y, max_y + 1)
    ]

    for x, y, dx, dy in stars:
        grid[y + dy * t - min_y][x + dx * t - min_x] = '#'

    for row in grid:
        print(''.join(row))


def main():
    stars = [parse_star(line) for line in stdin]
    max_fitness = get_fitness(stars, 0)
    min_fitness = max_fitness
    message_t = 0

    for t in range(1, maxsize):
        fitness = get_fitness(stars, t)

        if fitness > max_fitness:
            break

        if fitness < min_fitness:
            min_fitness = fitness
            message_t = t

    print_message(stars, message_t)


if __name__ == '__main__':
    main()

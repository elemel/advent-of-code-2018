from sys import stdin


def parse_star(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    x, y, dx, dy = [int(s) for s in number_line.split()]
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


def get_error_gradient(stars, t):
    return get_error(stars, t + 1) - get_error(stars, t - 1)


def print_message(stars, t):
    min_x, min_y, max_x, max_y = get_bounds(stars, t)
    grid = [(max_x - min_x + 1) * ['.'] for _ in range(max_y - min_y + 1)]

    for x, y, dx, dy in stars:
        grid[y + dy * t - min_y][x + dx * t - min_x] = '#'

    for row in grid:
        print(''.join(row))


def main():
    stars = [parse_star(line.strip()) for line in stdin]

    min_t = 0
    max_t = 1

    while get_error_gradient(stars, max_t) < 0:
        max_t *= 16

    while max_t - min_t >= 2:
        t = (min_t + max_t) // 2

        if get_error_gradient(stars, t) < 0:
            min_t = t
        else:
            max_t = t

    _, t = min((get_error(stars, t), t) for t in range(min_t, max_t + 1))
    print_message(stars, t)


if __name__ == '__main__':
    main()

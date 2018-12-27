from sys import stdin


def turn_on(grid, x, y):
    grid[y][x] += 1


def turn_off(grid, x, y):
    grid[y][x] = max(0, grid[y][x] - 1)


def toggle(grid, x, y):
    grid[y][x] += 2


def parse_instruction(line):
    number_line = ''.join(c if c.isdigit() else ' ' for c in line)
    x1, y1, x2, y2 = [int(s) for s in number_line.split()]

    if line.startswith('turn on '):
        return turn_on, x1, y1, x2, y2
    elif line.startswith('turn off '):
        return turn_off, x1, y1, x2, y2
    elif line.startswith('toggle '):
        return toggle, x1, y1, x2, y2


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    grid = [1000 * [0] for _ in range(1000)]

    for func, x1, y1, x2, y2 in instructions:
        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                func(grid, x, y)

    print(sum(sum(row) for row in grid))


if __name__ == '__main__':
    main()

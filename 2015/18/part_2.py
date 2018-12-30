from sys import stdin


def turn_corners_on(grid):
    width = len(grid[0])
    height = len(grid)

    for y in (0, height - 1):
        for x in (0, width - 1):
            grid[y][x] = '#'


def animate_cell(grid, x, y):
    width = len(grid[0])
    height = len(grid)

    x1 = max(0, x - 1)
    y1 = max(0, y - 1)
    x2 = min(x + 1, width - 1)
    y2 = min(y + 1, height - 1)

    neighbors_on = sum(
        grid[y3][x3] == '#'
        for x3 in range(x1, x2 + 1)
        for y3 in range(y1, y2 + 1)
        if (x3, y3) != (x, y))

    if grid[y][x] == '#':
        return '#' if neighbors_on in [2, 3] else '.'
    else:
        return '#' if neighbors_on == 3 else '.'


def main():
    grid = [list(line.strip()) for line in stdin]
    turn_corners_on(grid)

    for step in range(100):
        grid = [
            [animate_cell(grid, x, y) for x, cell in enumerate(row)]
            for y, row in enumerate(grid)
        ]

        turn_corners_on(grid)

    print(sum(cell == '#' for row in grid for cell in row))


if __name__ == '__main__':
    main()

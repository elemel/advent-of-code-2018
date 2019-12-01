from sys import stdin


def main():
    grid = [line.strip() for line in stdin]

    nodes = {
        (x, y): node
        for y, row in enumerate(grid)
        for x, node in enumerate(row)
        if node != '.'
    }

    x, y = len(grid[0]) // 2, len(grid) // 2
    dx, dy = 0, -1
    infection_count = 0

    for _ in range(10_000_000):
        node = nodes.get((x, y), '.')

        if node == '.':
            dx, dy = dy, -dx
            nodes[x, y] = 'W'
        elif node == 'W':
            nodes[x, y] = '#'
            infection_count += 1
        elif node == '#':
            dx, dy = -dy, dx
            nodes[x, y] = 'F'
        else:
            dx, dy = -dx, -dy
            del nodes[x, y]

        x += dx
        y += dy

    print(infection_count)


if __name__ == '__main__':
    main()

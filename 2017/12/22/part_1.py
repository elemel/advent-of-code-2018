from sys import stdin


def main():
    grid = [line.strip() for line in stdin]

    infected = {
        (x, y)
        for y, row in enumerate(grid)
        for x, node in enumerate(row)
        if node == '#'
    }

    x, y = len(grid[0]) // 2, len(grid) // 2
    dx, dy = 0, -1
    infection_count = 0

    for _ in range(10_000):
        if (x, y) in infected:
            dx, dy = -dy, dx
            infected.remove((x, y))
        else:
            dx, dy = dy, -dx
            infected.add((x, y))
            infection_count += 1

        x += dx
        y += dy

    print(infection_count)


if __name__ == '__main__':
    main()

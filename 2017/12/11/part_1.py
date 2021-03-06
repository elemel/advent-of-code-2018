from sys import stdin


def main():
    path = stdin.read().strip().split(',')

    # Cube grid: x + y + z == 0
    directions = dict(
        nw=(-1, 0, 1), n=(0, -1, 1), ne=(1, -1, 0),
        sw=(-1, 1, 0), s=(0, 1, -1), se=(1, 0, -1))

    x = 0
    y = 0
    z = 0

    for step in path:
        dx, dy, dz = directions[step]

        x += dx
        y += dy
        z += dz

    print((abs(x) + abs(y) + abs(z)) // 2)


if __name__ == '__main__':
    main()

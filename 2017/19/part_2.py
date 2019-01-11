from sys import stdin


def main():
    diagram = stdin.read().splitlines()
    x, y = diagram[0].index('|'), 0
    dx, dy = 0, 1
    step_count = 1

    while True:
        for new_dx, new_dy in [(dx, dy), (dy, -dx), (-dy, dx)]:
            if diagram[y + new_dy][x + new_dx] != ' ':
                dx, dy = new_dx, new_dy
                break
        else:
            break

        x += dx
        y += dy
        step_count += 1

    print(step_count)


if __name__ == '__main__':
    main()

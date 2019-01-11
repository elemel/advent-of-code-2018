from sys import stdin


def main():
    diagram = stdin.read().splitlines()
    x, y = diagram[0].index('|'), 0
    dx, dy = 0, 1
    letters = []

    while True:
        if diagram[y][x].isalpha():
            letters.append(diagram[y][x])

        for new_dx, new_dy in [(dx, dy), (dy, -dx), (-dy, dx)]:
            if diagram[y + new_dy][x + new_dx] != ' ':
                dx, dy = new_dx, new_dy
                break
        else:
            break

        x += dx
        y += dy

    print(''.join(letters))


if __name__ == '__main__':
    main()

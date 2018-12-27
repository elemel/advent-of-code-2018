from sys import stdin


directions = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}


def main():
    moves = stdin.read().strip()

    x = 0
    y = 0

    visited = {(0, 0)}

    for move in moves:
        dx, dy = directions[move]

        x += dx
        y += dy

        visited.add((x, y))

    print(len(visited))


if __name__ == '__main__':
    main()

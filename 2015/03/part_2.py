from sys import stdin


directions = {'^': (0, -1), 'v': (0, 1), '>': (1, 0), '<': (-1, 0)}


def main():
    moves = stdin.read().strip()

    xs = [0, 0]
    ys = [0, 0]

    visited = {(0, 0)}

    for i, move in enumerate(moves):
        j = i % 2
        dx, dy = directions[move]

        xs[j] += dx
        ys[j] += dy

        visited.add((xs[j], ys[j]))

    print(len(visited))


if __name__ == '__main__':
    main()

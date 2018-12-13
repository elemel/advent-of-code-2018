from heapq import heappop, heappush
from sys import stdin


directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}


curves = {
    ('<', '/'): 'v',
    ('<', '\\'): '^',

    ('>', '/'): '^',
    ('>', '\\'): 'v',

    ('^', '/'): '>',
    ('^', '\\'): '<',

    ('v', '/'): '<',
    ('v', '\\'): '>',
}


intersections = {
    ('<', 'left'): ('v', 'straight'),
    ('<', 'straight'): ('<', 'right'),
    ('<', 'right'): ('^', 'left'),

    ('>', 'left'): ('^', 'straight'),
    ('>', 'straight'): ('>', 'right'),
    ('>', 'right'): ('v', 'left'),

    ('^', 'left'): ('<', 'straight'),
    ('^', 'straight'): ('^', 'right'),
    ('^', 'right'): ('>', 'left'),

    ('v', 'left'): ('>', 'straight'),
    ('v', 'straight'): ('v', 'right'),
    ('v', 'right'): ('<', 'left'),
}


def main():
    squares = [list(line[:-1]) for line in stdin]

    carts = []

    for y, row in enumerate(squares):
        for x, square in enumerate(row):
            if square in '<>^v':
                track = '-' if square in '<>' else '|'
                heappush(carts, (1, y, x, square, track, 'left'))

    while carts:
        tick, y, x, cart, track, turn = heappop(carts)

        if squares[y][x] == 'X':
            continue

        squares[y][x] = track
        dx, dy = directions[cart]

        x += dx
        y += dy

        if squares[y][x] in '<>^v':
            squares[y][x] = 'X'
            print('%s,%s' % (x, y))
            return

        if squares[y][x] in '/\\':
            cart = curves[cart, squares[y][x]]

        if squares[y][x] == '+':
            cart, turn = intersections[cart, turn]

        track = squares[y][x]
        squares[y][x] = cart

        heappush(carts, (tick + 1, y, x, cart, track, turn))


if __name__ == '__main__':
    main()

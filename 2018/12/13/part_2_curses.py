import curses
from heapq import heapify, heappop, heappush
from sys import stdin
from time import sleep


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


def draw_squares(stdscr, squares):
    height, width = stdscr.getmaxyx()

    try:
        for y, row in enumerate(squares[:height]):
            for x, tile in enumerate(row[:width]):
                if tile == '-':
                    char = curses.ACS_HLINE
                elif tile == '|':
                    char = curses.ACS_VLINE
                elif tile == '+':
                    char = curses.ACS_PLUS
                elif tile == '/':
                    if x == 0 or row[x - 1] not in '-+<>':
                        char = curses.ACS_ULCORNER
                    else:
                        char = curses.ACS_LRCORNER
                elif tile == '\\':
                    if x == 0 or row[x - 1] not in '-+<>':
                        char = curses.ACS_LLCORNER
                    else:
                        char = curses.ACS_URCORNER
                else:
                    char = tile

                stdscr.addch(y, x, char, curses.color_pair(7))
    except:
        pass


def draw_carts(stdscr, carts, colors):
    height, width = stdscr.getmaxyx()

    for tick, y, x, cart, track, turn, color in carts:
        try:
            i = colors.index(color)
            stdscr.addch(y, x, cart, curses.color_pair(i))
        except:
            pass


def draw(stdscr, squares, carts, colors):
    draw_squares(stdscr, squares)
    draw_carts(stdscr, carts, colors)
    stdscr.move(0, 0)
    stdscr.refresh()
    sleep(0.05)


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)

    squares = [list(line[:-1]) for line in stdin]

    carts = []

    colors = [
        'black',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
    ]

    for y, row in enumerate(squares):
        for x, square in enumerate(row):
            if square in '<>^v':
                track = '-' if square in '<>' else '|'
                color = colors[1 + len(carts) % (len(colors) - 2)]
                heappush(carts, (1, y, x, square, track, 'left', color))

    max_tick = 0

    while carts:
        if carts[0][0] > max_tick:
            max_tick = carts[0][0]
            draw(stdscr, squares, carts, colors)

        tick, y, x, cart, track, turn, color = heappop(carts)

        squares[y][x] = track
        dx, dy = directions[cart]

        x += dx
        y += dy

        if squares[y][x] in '<>^v':
            for i, (_, y2, x2, _, track, _, _) in enumerate(carts):
                if x2 == x and y2 == y:
                    squares[y][x] = track
                    carts.pop(i)
                    heapify(carts)
                    break

            continue

        if squares[y][x] in '/\\':
            cart = curves[cart, squares[y][x]]

        if squares[y][x] == '+':
            cart, turn = intersections[cart, turn]

        track = squares[y][x]
        squares[y][x] = cart

        if not carts:
            print('%s,%s' % (x, y))
            print(max_tick)
            return

        heappush(carts, (tick + 1, y, x, cart, track, turn, color))


if __name__ == '__main__':
    curses.wrapper(main)

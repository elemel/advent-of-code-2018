from collections import deque
from sys import stdin


def rect(screen, a, b):
    for y in range(b):
        for x in range(a):
            screen[y][x] = '#'


def rotate_row(screen, a, b):
    screen[a].rotate(b)


def rotate_column(screen, a, b):
    column = [row[a] for row in screen]
    screen.rotate(-b)

    for row, pixel in zip(screen, column):
        row[a] = pixel

    screen.rotate(b)


def parse_instruction(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    a, b = [int(s) for s in number_line.split()]

    if line.startswith('rect '):
        return rect, a, b
    elif line.startswith('rotate row '):
        return rotate_row, a, b
    elif line.startswith('rotate column '):
        return rotate_column, a, b
    else:
        raise ValueError('Invalid instruction: {line}')


def main():
    instructions = [parse_instruction(line.strip()) for line in stdin]
    screen = deque(deque(50 * ['.']) for _ in range(6))

    for func, a, b in instructions:
        func(screen, a, b)

    for row in screen:
        print(''.join(row))


if __name__ == '__main__':
    main()

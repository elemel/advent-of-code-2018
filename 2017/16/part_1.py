from collections import deque
from sys import stdin


def parse_dance_move(s):
    if s.startswith('s'):
        x = int(s[1:])
        return 'spin', x
    elif s.startswith('x'):
        a, b = [int(s) for s in s[1:].split('/')]
        return 'exchange', a, b
    elif s.startswith('p'):
        a, b = s[1:].split('/')
        return 'partner', a, b
    else:
        raise ValueError(f'Invalid dance move: {s}')


def main():
    dance_moves = [parse_dance_move(s) for s in stdin.read().strip().split(',')]
    programs = deque('abcdefghijklmnop')

    for move in dance_moves:
        if move[0] == 'spin':
            _, x = move
            programs.rotate(x)
        elif move[0] == 'exchange':
            _, a, b = move
            programs[a], programs[b] = programs[b], programs[a]
        elif move[0] == 'partner':
            _, a, b = move
            i = programs.index(a)
            j = programs.index(b)
            programs[i], programs[j] = programs[j], programs[i]

    print(''.join(programs))


if __name__ == '__main__':
    main()

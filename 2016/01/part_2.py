from sys import stdin


directions = dict(E=(1, 0), N=(0, -1), S=(0, 1), W=(-1, 0))
turns = dict(EL='N', ER='S', NL='W', NR='E', SL='E', SR='W', WL='S', WR='N')


def parse_instruction(instruction_str):
    turn = instruction_str[0]
    walk = int(instruction_str[1:])
    return turn, walk


def main():
    instructions = [
        parse_instruction(s)
        for s in stdin.read().strip().split(', ')
    ]

    direction = 'N'
    x = 0
    y = 0
    visited = {(0, 0)}

    for turn, walk in instructions:
        direction = turns[direction + turn]
        dx, dy = directions[direction]

        for _ in range(walk):
            x += dx
            y += dy

            if (x, y) in visited:
                print(abs(x) + abs(y))
                return

            visited.add((x, y))


if __name__ == '__main__':
    main()

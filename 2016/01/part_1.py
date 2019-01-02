from sys import stdin


def parse_instruction(instruction_str):
    turn = -1 if instruction_str[0] == 'L' else 1
    walk = int(instruction_str[1:])
    return turn, walk


def main():
    instructions = [
        parse_instruction(s)
        for s in stdin.read().strip().split(', ')
    ]

    x = 0
    y = 0
    dx = 0
    dy = -1

    for turn, walk in instructions:
        dx, dy = -turn * dy, turn * dx
        x += walk * dx
        y += walk * dy

    print(abs(x) + abs(y))


if __name__ == '__main__':
    main()

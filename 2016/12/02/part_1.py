from sys import stdin


directions = dict(D=(0, 1), L=(-1, 0), R=(1, 0), U=(0, -1))


keypad = [
    '123',
    '456',
    '789',
]


def main():
    instruction_lines = [line.strip() for line in stdin]
    x, y = 1, 1
    bathroom_code = []

    for instruction_line in instruction_lines:
        for instruction in instruction_line:
            dx, dy = directions[instruction]
            x = min(max(0, x + dx), 2)
            y = min(max(0, y + dy), 2)

        bathroom_code.append(keypad[y][x])

    print(''.join(bathroom_code))


if __name__ == '__main__':
    main()

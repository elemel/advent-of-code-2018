from sys import stdin


directions = dict(D=(0, 1), L=(-1, 0), R=(1, 0), U=(0, -1))


keypad = [
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  ',
]


def main():
    instruction_lines = [line.strip() for line in stdin]
    x, y = 0, 2
    bathroom_code = []

    for instruction_line in instruction_lines:
        for instruction in instruction_line:
            dx, dy = directions[instruction]

            if 0 <= x + dx <= 4 and 0 <= y + dy <= 4:
                if keypad[y + dy][x + dx] != ' ':
                    x += dx
                    y += dy

        bathroom_code.append(keypad[y][x])

    print(''.join(bathroom_code))


if __name__ == '__main__':
    main()

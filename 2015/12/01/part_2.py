from sys import stdin


directions = {'(': 1, ')': -1}


def main():
    instructions = stdin.read().strip()
    floor = 0

    for i, instruction in enumerate(instructions, start=1):
        floor += directions[instruction]

        if floor == -1:
            print(i)
            return


if __name__ == '__main__':
    main()

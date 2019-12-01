from sys import stdin


directions = {'(': 1, ')': -1}


def main():
    instructions = stdin.read().strip()
    print(sum(directions[i] for i in instructions))


if __name__ == '__main__':
    main()

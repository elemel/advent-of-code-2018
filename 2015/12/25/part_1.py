from sys import maxsize, stdin


def main():
    line = stdin.read().strip()
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    target_row, target_column = [int(s) for s in number_line.split()]
    code = 20151125

    for start_row in range(2, maxsize):
        for column in range(1, start_row + 1):
            row = start_row - column + 1
            code *= 252533
            code %= 33554393

            if (row, column) == (target_row, target_column):
                print(code)
                return


if __name__ == '__main__':
    main()

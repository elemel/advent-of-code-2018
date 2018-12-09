from sys import stdin


def main():
    spreadsheet = [[int(s) for s in line.split()] for line in stdin]

    print(sum((x // y
        for row in spreadsheet
        for x in row
        for y in row
        if x > y and x % y == 0)))


if __name__ == '__main__':
    main()

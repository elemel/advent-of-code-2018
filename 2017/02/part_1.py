from sys import stdin


def main():
    spreadsheet = [[int(s) for s in line.split()] for line in stdin]
    print(sum(max(row) - min(row) for row in spreadsheet))


if __name__ == '__main__':
    main()

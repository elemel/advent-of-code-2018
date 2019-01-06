from sys import stdin


rules = {
    '^^.': '^',
    '.^^': '^',
    '^..': '^',
    '..^': '^',
}


def main():
    row = stdin.read().strip()
    rows = [row]

    while len(rows) < 40:
        padded_row = '.' + row + '.'

        row = ''.join(
            rules.get(padded_row[i:(i + 3)], '.') for i in range(len(row)))

        rows.append(row)

    print(sum(sum(tile == '.' for tile in row) for row in rows))


if __name__ == '__main__':
    main()

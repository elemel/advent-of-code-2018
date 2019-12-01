from sys import maxsize, stdin


def parse_disc(line):
    number_line = ''.join(c if c.isdigit() else ' ' for c in line)
    number, size, _, position = [int(s) for s in number_line.split()]
    return number, size, position


def main():
    discs = [parse_disc(line) for line in stdin]
    discs.append((7, 11, 0))

    for t in range(0, maxsize):
        for number, size, position in discs:
            if (t + number + position) % size != 0:
                break
        else:
            print(t)
            return


if __name__ == '__main__':
    main()

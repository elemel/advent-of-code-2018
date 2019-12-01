from sys import stdin


def parse_node(line):
    digit_line = ''.join(c if c.isdigit() else ' ' for c in line)
    x, y, _, used, avail, _ = [int(s) for s in digit_line.split()]
    return x, y, used, avail


def main():
    _, _, *node_lines = stdin.read().splitlines()
    nodes = [parse_node(line) for line in node_lines]

    print(sum(
        used_1 != 0 and (x1, y1) != (x2, y2) and used_1 <= avail_2
        for x1, y1, used_1, avail_1 in nodes
        for x2, y2, used_2, avail_2 in nodes))


if __name__ == '__main__':
    main()

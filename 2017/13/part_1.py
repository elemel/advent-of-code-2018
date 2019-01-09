from sys import stdin


def parse_layer(line):
    depth, range_ = [int(s) for s in line.split(': ')]
    return depth, range_


def main():
    layers = [parse_layer(line.strip()) for line in stdin]

    severity = sum(
        depth * range_
        for depth, range_ in layers
        if depth % (2 * (range_ - 1)) == 0)

    print(severity)


if __name__ == '__main__':
    main()

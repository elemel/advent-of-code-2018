from sys import maxsize, stdin


def parse_layer(line):
    depth, range_ = [int(s) for s in line.split(': ')]
    return depth, range_


def main():
    layers = [parse_layer(line.strip()) for line in stdin]

    for delay in range(0, maxsize):
        for depth, range_ in layers:
            if (delay + depth) % (2 * (range_ - 1)) == 0:
                break
        else:
            print(delay)
            return


if __name__ == '__main__':
    main()

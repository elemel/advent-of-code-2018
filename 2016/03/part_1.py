from sys import stdin


def parse_triangle(line):
    a, b, c = [int(s) for s in line.split()]
    return a, b, c


def is_possible_triangle(a, b, c):
    return a < b + c and b < c + a and c < a + b


def main():
    triangles = [parse_triangle(line.strip()) for line in stdin]
    print(sum(is_possible_triangle(a, b, c) for a, b, c in triangles))


if __name__ == '__main__':
    main()

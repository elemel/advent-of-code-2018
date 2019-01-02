from itertools import zip_longest
from sys import stdin


# https://docs.python.org/3/library/itertools.html
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def parse_triangle(line):
    a, b, c = [int(s) for s in line.split()]
    return a, b, c


def is_possible_triangle(a, b, c):
    return a < b + c and b < c + a and c < a + b


def main():
    row_triangles = [parse_triangle(line.strip()) for line in stdin]

    column_triangles = [
        column_triangle
        for triangle_triplet in grouper(row_triangles, 3)
        for column_triangle in zip(*triangle_triplet)
    ]

    print(sum(is_possible_triangle(a, b, c) for a, b, c in column_triangles))


if __name__ == '__main__':
    main()

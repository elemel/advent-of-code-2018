from sys import stdin


def parse_triangle(line):
    a, b, c = [int(s) for s in line.split()]
    return a, b, c


def is_possible_triangle(a, b, c):
    return a < b + c and b < c + a and c < a + b


def main():
    row_triangles = [parse_triangle(line.strip()) for line in stdin]

    triangle_triplets = [
        row_triangles[i:(i + 3)]
        for i in range(0, len(row_triangles), 3)
    ]

    column_triangles = [
        column_triangle
        for t1, t2, t3 in triangle_triplets
        for column_triangle in zip(t1, t2, t3)
    ]

    print(sum(is_possible_triangle(a, b, c) for a, b, c in column_triangles))


if __name__ == '__main__':
    main()

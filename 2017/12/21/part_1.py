from sys import stdin


def flip_pattern(pattern):
    return '/'.join(
        ''.join(reversed(pixel_row))
        for pixel_row in pattern.split('/'))


def rotate_pattern(pattern):
    pixel_rows = pattern.split('/')

    return '/'.join(
        ''.join(pixel_rows[y][x] for y in range(len(pixel_rows)))
        for x in range(len(pixel_rows) - 1, -1, -1))


def split_image(image, square_size):
    square_rows = []

    for y1 in range(0, len(image), square_size):
        square_rows.append([])

        for x1 in range(0, len(image), square_size):
            square_rows[-1].append(
                '/'.join(
                    ''.join(image[y2][x2] for x2 in range(x1, x1 + square_size))
                    for y2 in range(y1, y1 + square_size)))

    return square_rows


def join_image(square_rows, square_size):
    image_size = len(square_rows) * square_size
    image = [image_size * ['.'] for _ in range(image_size)]

    for y1, square_row in enumerate(square_rows):
        for x1, square in enumerate(square_row):
            pixel_rows = square.split('/')

            for y2, pixel_row in enumerate(pixel_rows):
                for x2, pixel in enumerate(pixel_row):
                    y = y1 * square_size + y2
                    x = x1 * square_size + x2
                    image[y][x] = pixel

    return image


def enhance_image(image, enhancement_rules):
    if len(image) % 2 == 0:
        square_size = 2
    else:
        square_size = 3

    square_rows = split_image(image, square_size)

    square_rows = [
        [enhancement_rules[square] for square in square_row]
        for square_row in square_rows
    ]

    return join_image(square_rows, square_size + 1)


def main():
    enhancement_rules = {}

    for line in stdin:
        key, value = line.strip().split(' => ')

        for _ in range(2):
            for _ in range(4):
                enhancement_rules[key] = value
                key = rotate_pattern(key)

            key = flip_pattern(key)

    image = [list('.#.'), list('..#'), list('###')]

    for _ in range(5):
        image = enhance_image(image, enhancement_rules)

    print(sum(sum(pixel == '#' for pixel in row) for row in image))


if __name__ == '__main__':
    main()

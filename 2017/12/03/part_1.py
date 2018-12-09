from sys import stdin


def spiral():
    i = 1
    n = 1
    x = 0
    y = 0

    yield i, x, y

    while True:
        for _ in range(n):
            i += 1
            x += 1
            yield i, x, y

        for _ in range(n):
            i += 1
            y += 1
            yield i, x, y

        n += 1

        for _ in range(n):
            i += 1
            x -= 1
            yield i, x, y

        for _ in range(n):
            i += 1
            y -= 1
            yield i, x, y

        n += 1


def main():
    square = int(stdin.read())

    for i, x, y in spiral():
        if i == square:
            print(abs(x) + abs(y))
            break


if __name__ == '__main__':
    main()

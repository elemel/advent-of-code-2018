from sys import stdin


def main():
    print(sum((int(line.strip()) for line in stdin)))


if __name__ == '__main__':
    main()

from sys import stdin


def main():
    document = stdin.read().strip()
    number_str = ''.join(c if c in '-0123456789' else ' ' for c in document)
    print(sum(int(s) for s in number_str.split()))


if __name__ == '__main__':
    main()

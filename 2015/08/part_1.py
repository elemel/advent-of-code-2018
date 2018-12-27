from ast import literal_eval
from sys import stdin


def main():
    string_literals = [line.strip() for line in stdin]
    strings = [literal_eval(l) for l in string_literals]
    print(sum(len(l) - len(s) for l, s in zip(string_literals, strings)))


if __name__ == '__main__':
    main()

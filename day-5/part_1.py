from sys import stdin


def reactive(a, b):
    return a != b and a.lower() == b.lower()


def main():
    arg = list(stdin.read().strip())
    arg.reverse()
    result = []

    while arg:
        if result and reactive(arg[-1], result[-1]):
            arg.pop()
            result.pop()
        else:
            result.append(arg.pop())

    print(len(result))



if __name__ == '__main__':
    main()

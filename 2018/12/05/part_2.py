from sys import stdin


def reactive(a, b):
    return a != b and a.lower() == b.lower()


def react(arg):
    arg = list(arg)
    arg.reverse()
    result = []

    while arg:
        if result and reactive(arg[-1], result[-1]):
            arg.pop()
            result.pop()
        else:
            result.append(arg.pop())

    return result


def main():
    units = list(stdin.read().strip())
    min_length = len(units)

    for removed_unit in 'abcdefghijklmnopqrstuvwxyz':
        filtered_units = [u for u in units if u.lower() != removed_unit]
        reacted_units = react(filtered_units)
        min_length = min(min_length, len(reacted_units))

    print(min_length)


if __name__ == '__main__':
    main()

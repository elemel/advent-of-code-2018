import json
from sys import stdin


def solve(obj):
    if type(obj) == int:
        return obj
    elif type(obj) == list:
        return sum(solve(element) for element in obj)
    elif type(obj) == dict:
        if 'red' in obj.values():
            return 0

        return sum(solve(value) for value in obj.values())
    else:
        return 0


def main():
    document = json.loads(stdin.read().strip())
    print(solve(document))


if __name__ == '__main__':
    main()

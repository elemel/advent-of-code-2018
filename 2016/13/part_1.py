from collections import deque
from sys import stdin


def memoized(func):
    results = {}

    def wrapper(*args):
        if args in results:
            return results[args]

        result = func(*args)
        results[args] = result
        return result

    return wrapper


def main():
    favorite_number = int(stdin.read().strip())
    locations = {}

    @memoized
    def is_open(x, y):
        n = x * x + 3 * x + 2 * x * y + y + y * y + favorite_number
        s = format(n, 'b').replace('0', '')
        return len(s) % 2 == 0

    queue = deque([(0, 1, 1)])
    visited = set()

    while queue:
        step, x, y = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if (x, y) == (31, 39):
            print(step)
            return

        for dx, dy in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            if x + dx >= 0 and y + dy >= 0 and is_open(x + dx, y + dy):
                queue.append((step + 1, x + dx, y + dy))


if __name__ == '__main__':
    main()

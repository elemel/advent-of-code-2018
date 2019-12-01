from collections import deque
from hashlib import md5
from sys import stdin


directions = [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]


def main():
    passcode = stdin.read().strip()
    queue = deque([('', 0, 0)])
    max_length = -1

    while queue:
        path, x, y = queue.popleft()

        if (x, y) == (3, 3):
            max_length = max(len(path), max_length)
            continue

        hasher = md5()
        hasher.update(passcode.encode('ascii'))
        hasher.update(path.encode('ascii'))
        digest = hasher.hexdigest()

        for digit, (direction, dx, dy) in zip(digest, directions):
            if digit in 'bcdef' and 0 <= x + dx <= 3 and 0 <= y + dy <= 3:
                queue.append((path + direction, x + dx, y + dy))

    print(max_length)


if __name__ == '__main__':
    main()

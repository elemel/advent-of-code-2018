from collections import deque
import hashlib
from sys import maxsize, stdin


def main():
    salt = stdin.read().strip()
    triplets = deque()
    quintuplets = {}
    keys = []

    for index in range(0, maxsize):
        hasher = hashlib.md5()
        hasher.update(salt.encode('ascii'))
        hasher.update(str(index).encode('ascii'))
        digest = hasher.hexdigest()

        for i in range(len(digest) - 2):
            if digest[i] == digest[i + 1] == digest[i + 2]:
                triplets.append((index, digest[i], digest))
                break

        for digit in '0123456789abcdef':
            if 5 * digit in digest:
                quintuplets[digit] = index

        if triplets:
            triplet_index, triplet_digit, triplet_digest = triplets[0]

            if index - triplet_index == 1000:
                triplets.popleft()
                quintuplet_index = quintuplets.get(triplet_digit, maxsize)

                if 1 <= quintuplet_index - triplet_index <= 1000:
                    keys.append(triplet_digest)

                    if len(keys) == 64:
                        print(triplet_index)
                        return


if __name__ == '__main__':
    main()

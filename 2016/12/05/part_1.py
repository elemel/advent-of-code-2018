import hashlib
from sys import maxsize, stderr, stdin


def main():
    door_id = stdin.read().strip()
    password = []

    for index in range(maxsize):
        hasher = hashlib.md5()
        hasher.update(door_id.encode('ascii'))
        hasher.update(str(index).encode('ascii'))
        digest = hasher.hexdigest()

        if digest.startswith('00000'):
            password.append(digest[5])

            if len(password) == 8:
                print(''.join(password))
                return

            print(''.join(password), file=stderr)


if __name__ == '__main__':
    main()

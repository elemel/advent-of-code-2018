import hashlib
from sys import maxsize, stderr, stdin


def main():
    door_id = stdin.read().strip()
    password = 8 * ['_']

    for index in range(maxsize):
        hasher = hashlib.md5()
        hasher.update(door_id.encode('ascii'))
        hasher.update(str(index).encode('ascii'))
        digest = hasher.hexdigest()

        if digest.startswith('00000'):
            if '0' <= digest[5] <= '7':
                position = int(digest[5])

                if password[position] == '_':
                    password[position] = digest[6]

                    if '_' not in password:
                        print(''.join(password))
                        return

                    print(''.join(password), file=stderr)


if __name__ == '__main__':
    main()

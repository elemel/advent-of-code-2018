import hashlib
from sys import maxsize, stdin


def main():
    secret_key = stdin.read().strip()

    for i in range(1, maxsize):
        m = hashlib.md5()
        m.update(secret_key.encode('ascii'))
        m.update(str(i).encode('ascii'))
        hash_ = m.hexdigest()

        if hash_.startswith('000000'):
            print(i)
            return


if __name__ == '__main__':
    main()

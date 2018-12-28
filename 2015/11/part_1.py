from sys import stdin


def increment_password(password):
    for i in range(len(password) - 1, -1, -1):
        if password[i] != 'z':
            password[i] = chr(ord(password[i]) + 1)
            break

        password[i] = 'a'


def validate_password(password):
    return (
        any(
            ord(password[i]) == ord(password[i + 1]) - 1 and
            ord(password[i + 1]) == ord(password[i + 2]) - 1
            for i in range(len(password) - 2)) and
        all(c not in 'iol' for c in password) and
        any(
            password[i] == password[i + 1] and
            password[j] == password[j + 1]
            for i in range(len(password) - 3)
            for j in range(i + 2, len(password) - 1)))


def main():
    password = list(stdin.read().strip())

    while True:
        increment_password(password)

        if validate_password(password):
            break

    print(''.join(password))


if __name__ == '__main__':
    main()

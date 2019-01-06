from collections import deque
from sys import stdin


def parse_operation(line):
    words = line.split()

    if line.startswith('swap position '):
        return 'swap_positions', int(words[2]), int(words[5])
    elif line.startswith('swap letter '):
        return 'swap_letters', words[2], words[5]
    elif line.startswith('rotate left '):
        return 'rotate', -int(words[2])
    elif line.startswith('rotate right '):
        return 'rotate', int(words[2])
    elif line.startswith('rotate based '):
        return 'rotate_special', words[-1]
    elif line.startswith('reverse positions '):
        return 'reverse_positions', int(words[2]), int(words[4])
    elif line.startswith('move position '):
        return 'move_position', int(words[2]), int(words[5])
    else:
        raise ValueError(f'Invalid operation: {line}')


def main():
    operations = [parse_operation(line.strip()) for line in stdin]
    password = deque('abcdefgh')

    for operation in operations:
        if operation[0] == 'swap_positions':
            _, x, y = operation
            password[x], password[y] = password[y], password[x]
        elif operation[0] == 'swap_letters':
            _, x, y = operation
            x = password.index(x)
            y = password.index(y)
            password[x], password[y] = password[y], password[x]
        elif operation[0] == 'rotate':
            _, x = operation
            password.rotate(x)
        elif operation[0] == 'rotate_special':
            _, x = operation
            x = password.index(x)
            password.rotate(1 + x + int(x >= 4))
        elif operation[0] == 'reverse_positions':
            _, x, y = operation

            while x < y:
                password[x], password[y] = password[y], password[x]
                x += 1
                y -= 1
        elif operation[0] == 'move_position':
            _, x, y = operation
            letter = password[x]
            del password[x]
            password.insert(y, letter)

    print(''.join(password))


if __name__ == '__main__':
    main()

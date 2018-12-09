from sys import stdin


def solve(chars, score):
    char = chars.pop()

    if char == '<':
        while char != '>':
            char = chars.pop()

            if char == '!':
                chars.pop()

        return 0

    total_score = score

    while chars[-1] != '}':
        total_score += solve(chars, score + 1)

        if chars[-1] == ',':
            chars.pop()

    chars.pop()
    return total_score


def main():
    chars = list(stdin.read().strip())
    chars.reverse()
    print(solve(chars, 1))


if __name__ == '__main__':
    main()

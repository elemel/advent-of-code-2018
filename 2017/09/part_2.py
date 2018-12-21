from sys import stdin


def solve(chars):
    score = 0
    char = chars.pop()

    if char == '<':
        while char != '>':
            char = chars.pop()

            if char == '!':
                chars.pop()
            elif char != '>':
                score += 1

        return score

    while chars[-1] != '}':
        score += solve(chars)

        if chars[-1] == ',':
            chars.pop()

    chars.pop()
    return score


def main():
    chars = list(stdin.read().strip())
    chars.reverse()
    print(solve(chars))


if __name__ == '__main__':
    main()

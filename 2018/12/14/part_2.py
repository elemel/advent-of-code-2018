from sys import stdin


def ends_with(scoreboard, sequence):
    return len(scoreboard) >= len(sequence) and all(
        scoreboard[i] == sequence[i] for i in range(-len(sequence), 0))


def main():
    scoreboard = [3, 7]
    sequence = [int(s) for s in stdin.read().strip()]
    elves = [0, 1]

    while True:
        total_score = sum(scoreboard[elf] for elf in elves)

        for digit_str in str(total_score):
            digit = int(digit_str)
            scoreboard.append(digit)

            if ends_with(scoreboard, sequence):
                print(len(scoreboard) - len(sequence))
                return

        for i, elf in enumerate(elves):
            elves[i] += 1 + scoreboard[elf]
            elves[i] %= len(scoreboard)


if __name__ == '__main__':
    main()

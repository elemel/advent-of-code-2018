from sys import stdin


def main():
    scoreboard = [3, 7]
    scoreboard_size = int(stdin.read().strip())
    elves = [0, 1]

    while len(scoreboard) < scoreboard_size + 10:
        total_score = sum(scoreboard[elf] for elf in elves)
        scoreboard.extend(int(s) for s in str(total_score))

        for i, elf in enumerate(elves):
            elves[i] += 1 + scoreboard[elf]
            elves[i] %= len(scoreboard)

    print(''.join(
        str(score)
        for score in scoreboard[scoreboard_size:scoreboard_size + 10]))


if __name__ == '__main__':
    main()

from collections import deque
from sys import stdin


def main():
    elf_count = int(stdin.read().strip())
    elves = deque([i + 1, 1] for i in range(elf_count))

    while len(elves) > 1:
        elf_number_1, present_count_1 = elves.popleft()
        elf_number_2, present_count_2 = elves.popleft()
        elves.append((elf_number_1, present_count_1 + present_count_2))

    elf_number, _ = elves.popleft()
    print(elf_number)


if __name__ == '__main__':
    main()

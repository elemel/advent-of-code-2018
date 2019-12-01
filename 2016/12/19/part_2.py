from collections import deque
from sys import stdin


def main():
    elf_count = int(stdin.read().strip())
    elves_1 = deque([i + 1, 1] for i in range(elf_count // 2))
    elves_2 = deque([i + 1, 1] for i in range(elf_count // 2, elf_count))

    while elves_1:
        elf_number_1, present_count_1 = elves_1.popleft()
        elf_number_2, present_count_2 = elves_2.popleft()
        elves_2.append((elf_number_1, present_count_1 + present_count_2))

        if len(elves_1) < (len(elves_1) + len(elves_2)) // 2:
            elves_1.append(elves_2.popleft())

    elf_number, _ = elves_2.popleft()
    print(elf_number)


if __name__ == '__main__':
    main()

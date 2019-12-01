from sys import stdin


def main():
    min_present_count = int(stdin.read().strip())    
    max_house_number = 1000000
    present_counts = (max_house_number + 1) * [0]

    for elf_number in range(1, max_house_number + 1):
        for i in range(1, 51):
            house_number = i * elf_number

            if house_number > max_house_number:
                break

            present_counts[house_number] += 11 * elf_number

    for house_number, present_count in enumerate(present_counts):
        if present_count >= min_present_count:
            print(house_number)
            return


if __name__ == '__main__':
    main()

from sys import stdin


def main():
    *replacement_lines, _, molecule = stdin.read().splitlines()
    replacements = [line.split(' => ') for line in replacement_lines]

    seen = set()

    for source, target in replacements:
        i = molecule.find(source)

        while i != -1:
            seen.add(molecule[:i] + target + molecule[i + len(source):])
            i = molecule.find(source, i + 1)

    print(len(seen))


if __name__ == '__main__':
    main()

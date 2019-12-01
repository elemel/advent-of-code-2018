from sys import stdin


def parse_program(line):
    words = line.split()

    if len(words) > 3:
        children = [word.strip(',') for word in words[3:]]
    else:
        children = []

    return words[0], children


def main():
    programs = [parse_program(line) for line in stdin]
    names = set(name for name, _ in programs)
    child_names = set(name for _, names in programs for name in names)
    print(list(names - child_names)[0])


if __name__ == '__main__':
    main()

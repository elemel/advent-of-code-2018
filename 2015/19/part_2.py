from sys import stdin


def main():
    *_, molecule = stdin.read().splitlines()
    molecule = molecule.replace('Rn', '(').replace('Y', ',').replace('Ar', ')')

    atom_count = sum(c.isupper() for c in molecule)
    comma_count = sum(c == ',' for c in molecule)

    print(atom_count - comma_count - 1)


if __name__ == '__main__':
    main()

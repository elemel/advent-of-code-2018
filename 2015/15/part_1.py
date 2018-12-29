from sys import stdin


CAPACITY = 0
DURABILITY = 1
FLAVOR = 2
TEXTURE = 3
CALORIES = 4


def parse_ingredient(line):
    number_line = ''.join(c if c in '-0123456789' else ' ' for c in line)
    properties = tuple(int(s) for s in number_line.split())
    assert(len(properties) == 5)
    return properties


def get_total_score(recipe, ingredients):
    total_properties = [0, 0, 0, 0, 0]

    for amount, ingredient in zip(recipe, ingredients):
        for i, value in enumerate(ingredient):
            total_properties[i] += amount * value

    total_score = 1

    for i, value in enumerate(total_properties):
        if i != CALORIES:
            total_score *= max(0, value)

    return total_score


def main():
    ingredients = [parse_ingredient(line.strip()) for line in stdin]
    assert(len(ingredients) == 4)
    max_total_score = 0

    for i in range(101):
        for j in range(101 - i):
            for k in range(101 - i - j):
                l = 100 - i - j - k
                recipe = i, j, k, l
                total_score = get_total_score(recipe, ingredients)
                max_total_score = max(total_score, max_total_score)

    print(max_total_score)


if __name__ == '__main__':
    main()

from sys import stdin


def get_cell_power(x, y, serial_number):
    rack_id = (x + 1) + 10
    power_level = rack_id * (y + 1)
    power_level += serial_number
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5
    return power_level


def main():
    serial_number = int(stdin.read())
    grid_size = 300

    cell_powers = [
        [get_cell_power(x, y, serial_number)
        for x in range(grid_size)]
        for y in range(grid_size)
    ]

    column_powers = [grid_size * [0] for _ in range(grid_size)]
    chosen = 0, 0, 0, 0

    for square_size in range(1, 301):
        for y in range(grid_size - square_size + 1):
            for x in range(grid_size):
                column_powers[y][x] += cell_powers[y + square_size - 1][x]

            for x in range(grid_size - square_size + 1):
                if x == 0:
                    square_power = sum(
                        column_powers[y][x] for x in range(square_size))
                else:
                    square_power -= column_powers[y][x - 1]
                    square_power += column_powers[y][x + square_size - 1]

                chosen = max(chosen, (square_power, x, y, square_size))

    _, chosen_x, chosen_y, chosen_size = chosen
    print('%s,%s,%s' % (chosen_x + 1, chosen_y + 1, chosen_size))


if __name__ == '__main__':
    main()

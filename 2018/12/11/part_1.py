from sys import stdin


def get_cell_power(x, y, serial_number):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial_number
    power_level *= rack_id
    power_level //= 100
    power_level %= 10
    power_level -= 5
    return power_level


def get_total_power(x, y, size, serial_number):
    return sum(
        get_cell_power(x2, y2, serial_number)
        for x2 in range(x, x + size)
        for y2 in range(y, y + size))


def main():
    serial_number = int(stdin.read())
    grid_size = 300
    square_size = 3

    _, chosen_x, chosen_y = max(
        (get_total_power(x, y, square_size, serial_number), x, y)
        for x in range(1, grid_size + 1 - square_size + 1)
        for y in range(1, grid_size + 1 - square_size + 1))

    print('%s,%s' % (chosen_x, chosen_y))


if __name__ == '__main__':
    main()

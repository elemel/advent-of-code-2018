from sys import stdin


def spiral():
	i = 1
	n = 1
	x = 0
	y = 0

	yield i, x, y

	while True:
		for _ in range(n):
			i += 1
			x += 1
			yield i, x, y

		for _ in range(n):
			i += 1
			y += 1
			yield i, x, y

		n += 1

		for _ in range(n):
			i += 1
			x -= 1
			yield i, x, y

		for _ in range(n):
			i += 1
			y -= 1
			yield i, x, y

		n += 1


def main():
	square = int(stdin.read())
	grid = {(0, 0): 1}

	for i, x, y in spiral():
		value = sum(grid.get((x2, y2), 0)
			for x2 in range(x - 1, x + 2)
			for y2 in range(y - 1, y + 2))

		if value > square:
			print(value)
			break

		grid[x, y] = value


if __name__ == '__main__':
	main()

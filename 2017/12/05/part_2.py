from sys import stdin


def main():
	instructions = [int(line) for line in stdin]

	step = 0
	address = 0

	while 0 <= address < len(instructions):
		step += 1
		offset = instructions[address]

		if offset >= 3:
			instructions[address] -= 1
		else:
			instructions[address] += 1

		address += offset

	print(step)


if __name__ == '__main__':
	main()

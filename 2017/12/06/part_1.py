from sys import stdin


def main():
	banks = [int(s) for s in stdin.read().split()]
	seen = set()

	while tuple(banks) not in seen:
		seen.add(tuple(banks))

		size, i = max((size, -i) for i, size in enumerate(banks))
		i = -i
		banks[i] = 0

		while size:
			i = (i + 1) % len(banks)
			size -= 1
			banks[i] += 1

	print(len(seen))


if __name__ == '__main__':
	main()

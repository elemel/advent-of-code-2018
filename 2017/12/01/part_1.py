from sys import stdin


def main():
	digits = [int(s) for s in stdin.read().strip()]
	next_digits = digits[1:] + digits[:1]
	print(sum(a for a, b in zip(digits, next_digits) if a == b))


if __name__ == '__main__':
	main()

from sys import stdin


def main():
	digits = [int(s) for s in stdin.read().strip()]

	print(sum(digit
		for i, digit in enumerate(digits)
		if digit == digits[i - len(digits) // 2]))


if __name__ == '__main__':
	main()

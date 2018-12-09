from sys import stdin


def validate(passphrase):
	return len(set(passphrase)) == len(passphrase)


def main():
	passphrases = [line.split() for line in stdin]
	print(sum(validate(passphrase) for passphrase in passphrases))


if __name__ == '__main__':
	main()

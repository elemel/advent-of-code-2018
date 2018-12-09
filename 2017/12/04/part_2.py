from sys import stdin


def sort_word(word):
	return ''.join(sorted(list(word)))


def validate(passphrase):
	return len(set(sort_word(word) for word in passphrase)) == len(passphrase)


def main():
	passphrases = [line.split() for line in stdin]
	print(sum(validate(passphrase) for passphrase in passphrases))


if __name__ == '__main__':
	main()

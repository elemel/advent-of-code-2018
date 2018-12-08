from sys import stdin


def solve(node):
	child_count = node.pop()
	metadata_count = node.pop()

	return (sum(solve(node) for _ in range(child_count)) +
		sum(node.pop() for _ in range(metadata_count)))


def main():
	node = [int(s) for s in stdin.read().split()]
	node.reverse()
	print(solve(node))


if __name__ == '__main__':
	main()

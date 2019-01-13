def main():
    print(sum(
        any(b % d == 0 for d in range(2, b))
        for b in range(106500, 123517, 17)))


if __name__ == '__main__':
    main()

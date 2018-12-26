def main():
    f = 10551345
    a = sum(b for b in range(1, f + 1) if f % b == 0)
    print(a)


if __name__ == '__main__':
    main()

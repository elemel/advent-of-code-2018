from sys import stdin


def split_ip(ip):
    j = 0

    for i, c in enumerate(ip):
        if c in '[]':
            yield ip[j:i]
            j = i + 1

    yield ip[j:]


def find_abas(ip):
    for i in range(len(ip) - 2):
        if ip[i + 1] != ip[i] and ip[i + 2] == ip[i]:
            yield ip[i:(i + 3)]


def to_bab(aba):
    a, b, _ = list(aba)
    return b + a + b


def supports_ssl(ip):
    abas = set()
    babs = set()

    for i, part in enumerate(split_ip(ip)):
        for aba in find_abas(part):
            if i % 2 == 0:
                abas.add(aba)
            else:
                babs.add(aba)

    return any(to_bab(aba) in babs for aba in abas)


def main():
    ips = [line.strip() for line in stdin]
    print(sum(supports_ssl(ip) for ip in ips))


if __name__ == '__main__':
    main()

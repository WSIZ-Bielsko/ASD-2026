


if __name__ == '__main__':
    with open('../assets/200k.txt') as f:
        lns = f.readlines()
        for ln in lns[:50]:
            print(ln.strip())
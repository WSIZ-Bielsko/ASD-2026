


if __name__ == '__main__':
    x = 12313
    print(bin(x))
    x = (x>>3)
    print(bin(x))
    # problem -- 6 przedmiotow ktore mozna "wziac lub nie"

    # 111111  ... czyli 2**N - 1
    x = 2**6 - 1
    print(bin(x))

    while x>0:
        print(bin(x), x)
        x -= 1
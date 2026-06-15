

def val_1_at(mask: int, pos: int) -> bool:
    return bool(mask & (1 << pos))


if __name__ == '__main__':
    x = 0b1010
    print(x)    # 8
    print(bin(x)) # 0b1010

    print(x>>3 & 1) # 1
    print(x>>2 & 1) # 0
    print(x>>1 & 1) # 1
    print(x>>0 & 1) # 0

    print('--------')
    print(val_1_at(x, 3))
    print(val_1_at(x, 2))

    # (n & -n).bit_length() - 1

    x = 0b1010000  # -> 4
    print((x & -x).bit_length() - 1)
    print(' ' + bin(x))
    print(bin(-x))


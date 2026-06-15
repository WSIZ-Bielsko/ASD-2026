import random
import struct

from sortedcontainers import SortedSet

from asd_2026.common.utils import ts, duration


def gen_data(min_val: float, max_val:float, n_elems: int) -> list[float]:
    return [random.uniform(min_val, max_val) for _ in range(n_elems)]


def save_data_to_binary_file(filename: str, data: list[tuple[float]]):
    with open(filename, 'wb') as f:
        for item in data:
            f.write(struct.pack('d', item[0]))

def load_data_from_binary_file(filename: str) -> list[tuple[float]]:
    with open(filename, 'rb') as f:
        data = []
        while True:
            try:
                value = struct.unpack('d', f.read(8))[0]
                data.append((value,))
            except struct.error:
                break
        return data


def find_in_range(min_val, max_val, data) -> list[float] :
    return  [ min_val <= v <= max_val for v in data]

def find_in_range_ss(min_val, max_val, data: SortedSet) -> list[float] :
    return  list(data.irange(min_val, max_val))

if __name__ == '__main__':
    st = ts()
    zz = gen_data(0, 10, 5 * 10**6)
    print(f'generated in {duration(st)}')


    # generate 1000 test positions (numbers between 0 and 10), and for each find all the points in data which
    # are in range (pos - 1, pos + 1)

    test_data = gen_data(0, 10, 10)

    st = ts()
    res = [ find_in_range(pos - 0.1, pos + 0.1, zz) for pos in test_data]
    print(f'found simple in {duration(st)}')

    st = ts()
    ss = SortedSet(zz)
    print(f'generated SortedSet in {duration(st)}')

    st = ts()
    res = [ find_in_range_ss(pos - 0.1, pos + 0.1, ss) for pos in test_data]
    print(f'found SS in {duration(st)}')





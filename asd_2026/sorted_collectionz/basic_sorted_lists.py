from random import randint

from asd_2026.common.utils import ts, duration


state = 42  # Seed

def random():
    global state
    state = (1103515245 * state + 12345) % 2**31
    return state



def create_users(n: int) -> list[str]:
    return [f'u{random()}' for _ in range(n)]


def bench(start: int, steps: int):
    # st = ts()
    N = start
    for _ in range(steps):
        uu = create_users(N)
        # print(f'creation of {N} users took: {duration(st)} seconds')
        st = ts()
        uu.sort()
        print(f'sorting {N:10} users took: {duration(st)} seconds')
        N *= 2



def find_it(data: list, val):
    if len(data)==0 or val > data[-1]:
        return -1
    if val < data[0]:
        return data[0]

    a = 0
    b = len(data) - 1
    # mamy pewnosc, ze data[b] > val
    while b - a > 1:
        mi = (a + b) // 2
        if val < data[mi]:
            b = mi
        else:
            a = mi

    if data[a] == val:
        return val
    return data[b]

import pytest

def test_int_exact_match_returns_that_value():
    assert find_it([2, 4, 6, 7, 8], 6) == 6

def test_int_between_values_returns_next_greater():
    assert find_it([2, 4, 6, 7, 8], 5) == 6

def test_int_first_element_equal():
    assert find_it([2, 4, 6, 7, 8], 2) == 2

def test_int_smaller_than_all_returns_first():
    assert find_it([2, 4, 6, 7, 8], 1) == 2

def test_int_greater_than_all_returns_minus_one():
    assert find_it([2, 4, 6, 7, 8], 12) == -1

def test_int_empty_list_returns_minus_one():
    assert find_it([], 10) == -1

def test_int_with_negative_numbers():
    assert find_it([-10, -5, 0, 3, 9], -6) == -5

def test_string_exact_match_returns_that_string():
    assert find_it(["ala", "bartek", "celina", "darek"], "celina") == "celina"

def test_string_between_values_returns_next_alphabetically():
    assert find_it(["ala", "bartek", "celina", "darek"], "basia") == "celina"

def test_string_greater_than_all_returns_minus_one():
    assert find_it(["ala", "bartek", "celina", "darek"], "zenon") == -1

if __name__ == '__main__':
    bench(1000, 13)
    # print(uu)
    # print(len(set(uu)))

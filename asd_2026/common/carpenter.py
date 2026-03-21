from random import randint, seed


def assemble_from_two(data, M):
    gg = [0] * (10 ** 6)
    for x in data:
        gg[x] += 1
    res = 0
    for i in range(1, M // 2):
        res += min(gg[i], gg[M - i])
    if M % 2 == 0:
        res += gg[M // 2] // 2
    return res


def megalegar(data: list, m: int) -> int:
    data.sort()
    ans = []
    i, j = 0, len(data) - 1
    while i != j:
        if data[i] + data[j] == m:
            ans.append((data[i], data[j]))
            data = data[i:j]
            j = len(data) - 1
            i = 0
        elif data[i] + data[j] > m:
            j -= 1
        elif data[i] + data[j] < m:
            i += 1
    return len(ans)


def test_simple():
    assert assemble_from_two([1,2,5,5,7,9], 10) == 2


def test_thousand():
    assert assemble_from_two([1] * 1000 + [2] * 1000 + [8] * 1000 + [9] * 1000, 10) == 2000

def test_four_thousand():
    w = [1] * 1000 + [2] * 1000 + [3] * 1000 + [4] * 1000 + [5] * 1000 + [6] * 1000 + [7] * 1000 + [8] * 1000 + [9] * 1000
    r = assemble_from_two(w, 10)
    assert r == 4500

def test_basic_example():
    """Example from the problem statement."""
    data = [1, 2, 5, 5, 7, 9]
    assert assemble_from_two(data, 10) == 2


def test_duplicate_pieces_same_value():
    """Four identical pieces should yield two megalegars (5+5, 5+5)."""
    data = [5, 5, 5, 5]
    assert assemble_from_two(data, 10) == 2


def test_no_valid_pairs():
    """No two pieces sum to M — result must be 0."""
    data = [1, 2, 3]
    assert assemble_from_two(data, 10) == 0

def test_random():
    seed(111)
    w = [randint(0, 10 ** 5) for _ in range(10 ** 6)]
    r = assemble_from_two(w, 12345)
    assert r == 50922

def test_single_piece_exact_length():
    """A single piece exactly equal to M cannot be used (need 2 pieces)."""
    data = [10, 1, 2]
    assert assemble_from_two(data, 10) == 0


def test_empty_list():
    """Empty input should return 0."""
    data = []
    assert assemble_from_two(data, 10) == 0


def test_single_element():
    """One piece cannot form a pair."""
    data = [5]
    assert assemble_from_two(data, 10) == 0


def test_greedy_order_independence():
    """Multiple valid pairings — only max count matters, not pairing order."""
    # (1,9), (3,7) — two valid pairs
    data = [1, 3, 7, 9]
    assert assemble_from_two(data, 10) == 2


def test_pieces_larger_than_M():
    """Pieces exceeding M individually cannot contribute to any pair."""
    data = [11, 12, 1, 9]
    assert assemble_from_two(data, 10) == 1


def test_multiple_same_pairs_limited_by_count():
    """Only one pair (5,5) possible when there are only two 5s."""
    data = [5, 5, 3, 4]
    assert assemble_from_two(data, 10) == 1


def test_large_input_count():
    """Stress test: 1000 pairs of (1,9) should yield 1000."""
    data = [1] * 1000 + [9] * 1000
    assert assemble_from_two(data, 10) == 1000


def test_large_mixed_pairs():
    """
    100 pieces of value 3, 100 of value 7, 50 of value 2, 50 of value 8.
    Pairs: (3,7) x100, (2,8) x50 → 150 total.
    """
    data = [3] * 100 + [7] * 100 + [2] * 50 + [8] * 50
    assert assemble_from_two(data, 10) == 150


def test_large_unbalanced_supply():
    """
    500 pieces of value 1, but only 200 pieces of value 9.
    Pairs (1,9) capped at 200 by the scarcer side.
    Remaining 300 ones pair with nothing.
    """
    data = [1] * 500 + [9] * 200
    assert assemble_from_two(data, 10) == 200

if __name__ == '__main__':
    r = assemble_from_two([1,2,5,5,7,9], 10)
    # r = megalegar([1] * 1000 + [2] * 1000 + [8] * 1000 + [9] * 1000, 10)

    # seed(111)
    # w = [randint(0, 10 ** 5) for _ in range(10 ** 6)]
    # print(w[:10])
    # r = megalegar(w, 12345)
    print(r)

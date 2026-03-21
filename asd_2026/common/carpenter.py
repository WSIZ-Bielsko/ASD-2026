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

def test_random():
    seed(111)
    w = [randint(0, 10 ** 5) for _ in range(10 ** 6)]
    r = assemble_from_two(w, 12345)
    assert r == 50922

if __name__ == '__main__':
    r = assemble_from_two([1,2,5,5,7,9], 10)
    # r = megalegar([1] * 1000 + [2] * 1000 + [8] * 1000 + [9] * 1000, 10)

    # seed(111)
    # w = [randint(0, 10 ** 5) for _ in range(10 ** 6)]
    # print(w[:10])
    # r = megalegar(w, 12345)
    print(r)

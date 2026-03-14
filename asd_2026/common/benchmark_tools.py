import random
from collections import deque

from asd_2026.common.utils import ts, duration


def get_dataset(data) -> list[int]:
    n_elems = data[0]
    mx = data[1]
    # generate a list of random numbers between 0 and MX (ex)
    return [random.randint(0, mx - 1) for _ in range(n_elems)]


def ksef1(data) -> int:
    kolejka = []
    for elem in data:
        kolejka.append(elem)
    ss = 0
    while len(kolejka) > 0:
        ss += kolejka[0]
        kolejka = kolejka[1:]
    return ss


def ksef2(data) -> int:
    kolejka = deque()
    for elem in data:
        kolejka.append(elem)
    ss = 0
    while len(kolejka) > 0:
        ss += kolejka.popleft()
    return ss

def perf(function, data) -> float:
    """
    Run function on data and return execution time.
    :param function:
    :param data:
    :return:
    """
    st = ts()
    function(data)
    return ts() - st


def benchmark(function, data, n_threads=1, repetitions= 10) -> tuple[float, float, float]:
    """
    Run function on data; use n_threads; each run is repeated repetitions times.
    Return median, lower 25%, upper 75% of execution times.


    :param function:
    :param data:
    :param n_threads:
    :param repetitions:
    :return:
    """

    from concurrent.futures import ProcessPoolExecutor, wait

    res = []
    e = ProcessPoolExecutor(n_threads)
    for i in range(repetitions):
        res.append(e.submit(perf, function, data))
    wait(res)
    res = [r.result() for r in res]
    res.sort()
    n = len(res)
    return res[n // 2], res[n // 4], res[n * 3 // 4]

def format_median(res):
    return f'{res[0]:.3f} ({res[1]:.3f}, {res[2]:.3f})'

if __name__ == '__main__':
    st = ts()
    n = 8 * 10 ** 6
    # d = get_dataset(n, 100)
    # print(f'generating {n} numbers took {duration(st)}s')

    # zz = benchmark(get_dataset, (n, 100) , n_threads=24, repetitions=100)
    # print(f'generating {n} numbers took {format_median(zz)}s')

    data = list(range(n))
    zz = benchmark(ksef2, data, n_threads=8, repetitions=100)
    print(f'ksef1 {n} numbers took {format_median(zz)}s')


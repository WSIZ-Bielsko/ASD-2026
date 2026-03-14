from collections import deque

from asd_2026.common.benchmark_tools import benchmark, format_median
from asd_2026.common.plotz import DataPoint, plot


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


if __name__ == '__main__':
    n = 200
    results = []
    x = []
    while n < 10**4:
        print(f'generating {n} numbers')
        data = list(range(n))
        zz = benchmark(ksef2, data, n_threads=8, repetitions=80)
        # zz = (n, n*0.9, n*1.1)
        results.append(DataPoint(mean=zz[0], lower=zz[1], upper=zz[2]))
        x.append(n)
        print(f'ksef2 {n} numbers took {format_median(zz)}s')
        n = int(n * 1.1)
    plot(results, x, "n", "time (s)", "ksef2")




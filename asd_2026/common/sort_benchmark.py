from random import randint

from asd_2026.common.benchmark_tools import benchmark, format_median
from asd_2026.common.plotz import DataPoint, plot


def python_sort(data):
    data.sort()
    return data


if __name__ == '__main__':

    numbers = [randint(0, 10 ** 9) for _ in range(10 ** 7)]

    n = 200
    results = []
    x = []

    while n < 2 * 10 ** 6:
        print(f'profiling for {n=}')

        data = numbers[:n]

        # data = list(range(n))
        # data = deque(data)
        # here create data as either: a list, or a deque
        zz = benchmark(python_sort, data, n_threads=8, repetitions=80)
        # zz = (n, n*0.9, n*1.1)
        results.append(DataPoint(mean=zz[0], lower=zz[1], upper=zz[2]))
        x.append(n)
        print(f'sort {n} numbers took {format_median(zz)}s')
        n = int(n * 1.1)
    plot(results, x, "n", "time (s)", "sort")

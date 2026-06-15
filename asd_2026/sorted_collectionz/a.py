from random import randint, seed

from sortedcontainers import SortedSet




if __name__ == '__main__':
    seed(111)
    N = 10**1
    uu = [randint(0,10**8) for _ in range(N)]

    ss = SortedSet(uu)
    print(ss)
    el = ss.bisect_left(28556580)  #index where value is >= 28556581
    print(el)

    zz = ss.irange(26066268, 55964948)
    for z in zz:
        print(z)



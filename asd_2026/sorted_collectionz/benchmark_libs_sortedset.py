from random import randint, seed

from sortedcontainers import SortedSet

from asd_2026.common.utils import ts, duration
from asd_2026.sorted_collectionz.basic_sorted_lists import create_users
from BTrees.OOBTree import OOSet



"""
SortedSet:

n=     20000 creation: 0.010 add: 0.020 remove: 0.021 
n=     40000 creation: 0.020 add: 0.021 remove: 0.021 
n=     80000 creation: 0.056 add: 0.026 remove: 0.024 
n=    160000 creation: 0.128 add: 0.028 remove: 0.027 
n=    320000 creation: 0.332 add: 0.031 remove: 0.033 
n=    640000 creation: 0.634 add: 0.032 remove: 0.034 
n=   1280000 creation: 1.728 add: 0.038 remove: 0.036 
n=   2560000 creation: 3.940 add: 0.045 remove: 0.040 


OOSet:
n=     20000 creation: 0.032 add: 0.032 remove: 0.030 
n=     40000 creation: 0.092 add: 0.051 remove: 0.049 
n=     80000 creation: 0.335 add: 0.095 remove: 0.093 
n=    160000 creation: 1.334 add: 0.177 remove: 0.176 
n=    320000 creation: 5.232 add: 0.336 remove: 0.329 
n=    640000 creation: 21.223 add: 0.660 remove: 0.652 
n=   1280000 creation: 102.243 add: 1.967 remove: 1.786 


Rust - Release:
n=20000    creation: 0.0027 add: 0.0030 remove: 0.0024
n=40000    creation: 0.0056 add: 0.0035 remove: 0.0038
n=80000    creation: 0.0122 add: 0.0042 remove: 0.0032
n=160000   creation: 0.0257 add: 0.0059 remove: 0.0039
n=320000   creation: 0.0659 add: 0.0090 remove: 0.0060
n=640000   creation: 0.2143 add: 0.0143 remove: 0.0093
n=1280000  creation: 0.5309 add: 0.0160 remove: 0.0103
n=2560000  creation: 1.2418 add: 0.0172 remove: 0.0117


"""


def create_sortedset(data):
    return SortedSet(data)

def create_ooset(data):
    return OOSet(data)



def bench(n, creator):
    main_corpus = create_users(n)
    extr_corpus = create_users(10000)
    st = ts()
    ss = creator(main_corpus)
    print(f'n={n:10} creation: {duration(st)} ', end='')
    st = ts()
    for uu in extr_corpus:
        ss.add(uu)
    print(f'add: {duration(st)} ', end='')
    st = ts()
    for uu in extr_corpus:
        ss.remove(uu)
    print(f'remove: {duration(st)} ')




if __name__ == '__main__':


    xx = 10000
    for i in range(10,18):
        xx = int(xx * 2)
        bench(xx, create_ooset)
        # bench(xx, create_sortedset)

    # seed(111)
    # N = 10**1
    # uu = [randint(0,10**8) for _ in range(N)]
    #
    # ss = SortedSet(uu)
    # print(ss)
    # el = ss.bisect_left(28556582)
    # print(el)

    #todo: do zmierzenia:
    # insert i removal z ss sa typu O(log n)



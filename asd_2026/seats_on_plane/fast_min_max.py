import heapq

from asd_2026.common.utils import ts


class MinStore:
    def __init__(self):
        self.pq = []
        self.removed = set()

    def push(self, val):
        heapq.heappush(self.pq, val)
        if val in self.removed:
            self.removed.remove(val)

    def remove(self, val):
        self.removed.add(val)

    def min(self):
        rr = []
        while self.pq[0] in self.removed:
            rr.append(self.pq[0])
            heapq.heappop(self.pq)
        self.removed.difference_update(rr)
        return self.pq[0]



def test_bench1():
    store = MinStore()
    for i in range(10**6):
        store.push(i)

    st = ts()
    for _ in range(10**6, 10**6 + 10000):
        store.push(_)
        mm = store.min()
    en = ts()
    print(f"Time taken: {en - st:.6f} seconds") # 0.007

def test_bench2():
    store = []
    for i in range(10**6):
        store.append(i)

    st = ts()
    for _ in range(10**6, 10**6 + 10000):
        store.append(_)
        mm = min(store)
    en = ts()
    print(f"Time taken: {en - st:.3f} seconds") # 400



if __name__ == '__main__':
    store = MinStore()

    store.push(1)
    print(store.min()) # 1

    store.push(2)
    print(store.min()) # 1

    store.push(0)
    print(store.min()) # 0

    store.remove(0)
    print(store.min()) # 1

    store.remove(1)
    print(store.min()) # 2
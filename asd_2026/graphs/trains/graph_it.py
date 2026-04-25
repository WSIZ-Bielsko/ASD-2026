from collections import defaultdict

from PIL.ImageChops import offset

OFFSET = 1000


def to_graph(upper: list[int], lower: list[int]) -> dict[int, list[int]]:
    d = defaultdict(lambda: [])
    prev = None
    n = len(upper)
    for i in range(n):
        if upper[i] == 1:
            if prev is not None:
                d[prev].append(i)
            prev = i
        if upper[i] == 1 and lower[i] == 1:
            d[i].append(OFFSET + i)
            d[OFFSET + i].append(i)

    prev = None
    for i in range(n - 1, -1, -1):
        if lower[i] == 1:
            if prev is not None:
                d[OFFSET+prev].append(OFFSET+i)
            prev = i
    return d


def dfs_can_reach(start: int, alice: int, graph: dict, visited: set) -> bool:
    print(f'visiting {start}, {alice=}')
    if start == alice or start == OFFSET + alice or start + OFFSET == alice:
        print(f'found alice {start}')
        return True
    visited.add(start)
    for n in graph[start]:
        if n in visited:
            continue
        if dfs_can_reach(n, alice, graph, visited):
            return True
    return False


if __name__ == '__main__':
    dd = to_graph([1, 1, 0, 1, 1], [1, 0, 0, 0, 1])
    for k in dd:
        print(k, dd[k])

    start = 3
    alice = 1
    print(dfs_can_reach(0, alice, dd, set()))
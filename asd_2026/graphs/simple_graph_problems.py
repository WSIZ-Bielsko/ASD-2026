from asd_2026.graphs.a import get_symmetric_graph
from asd_2026.graphs.graph_tools import Graph


def dfs(g: Graph, start: int, visited: set):
    print(f'entering {start}')
    if start in visited:
        return
    visited.add(start)
    for neighbor in g[start]:
        dfs(g, neighbor, visited)


if __name__ == '__main__':
    g: Graph = {
        2: [7, 5],
        4: [],
        5: [9],
        6: [15, 11],
        7: [12, 10, 6],
        9: [4],
        10: [],
        11: [],
        12: [],
        15: []
    }
    g = get_symmetric_graph(g)
    visited = set()
    dfs(g, 2, visited)
    print(visited)

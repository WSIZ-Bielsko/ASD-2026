from dataclasses import dataclass

@dataclass
class Edge:
    dst: int
    weight: int


def get_neighbors(g: dict[int, list[Edge]]) -> dict[int, list[int]]:
    res = {}
    for k in g.keys():
        res[k] = [e.dst for e in g[k]]
    return res


def print_matrix(matrix: list[list[int]]) -> None:
    N = len(matrix)
    for i in range(N):
        for j in range(N):
            print(f'{matrix[i][j]:4}', end='')
        print()


def get_matrix(g: dict[int,list[Edge]]) -> list[list[int]]:
    N = len(g)
    matrix = [[9999]*N for _ in range(N)]
    for k in g.keys():
        for e in g[k]:
            matrix[k][e.dst] = e.weight
    return matrix


def get_near_neighbors(graph: dict[int, list[int]], start: int, depth: int, visited: set[int]):
    print(f'entering {start}')
    visited.add(start)
    if depth == 0:
        return
    for neighbor in graph[start]:
        # if neighbor in visited:
        #     continue (won't allow to enter node if shorter path found)
        get_near_neighbors(graph, neighbor, depth-1, visited)
    return visited





if __name__ == '__main__':
    g: dict[int, list[Edge]] = {
        0: [Edge(1, 4), Edge(7, 8)],
        1: [Edge(0, 4), Edge(2, 8), Edge(7, 11)],
        2: [Edge(1, 8), Edge(3, 7), Edge(5, 4), Edge(8, 2)],
        3: [Edge(2, 7), Edge(4, 9), Edge(5, 14)],
        4: [Edge(3, 9), Edge(5, 10)],
        5: [Edge(2, 4), Edge(3, 14), Edge(4, 10), Edge(6, 2)],
        6: [Edge(5, 2), Edge(7, 1), Edge(8, 6)],
        7: [Edge(0, 8), Edge(1, 11), Edge(6, 1), Edge(8, 7)],
        8: [Edge(2, 2), Edge(6, 6), Edge(7, 7)]
    }

    gg = get_neighbors(g)

    vis = set()
    get_near_neighbors(gg, start=0, depth=2, visited=vis)
    print('visited=',sorted(list(vis)))


    print(gg)
    N = len(g)
    m = get_matrix(g)
    print_matrix(m)

    print('---ALGO IN QUESTION-----')
    # Floyd–Warshall
    for s in range(N):
        for k in range(N):
            for d in range(N):
                if m[s][k] + m[k][d] < m[s][d]:
                    m[s][d] = m[s][k] + m[k][d]

    print_matrix(m)
    print(m[2][7]) # 7
    print(m[3][7]) # 14

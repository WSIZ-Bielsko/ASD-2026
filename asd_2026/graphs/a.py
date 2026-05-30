from collections import defaultdict

type Graph = dict[int, list[int]]

def get_symmetric_graph(graph: Graph) -> Graph:
    res = defaultdict(lambda :[])
    for src in graph.keys():
        if src not in res:
            res[src] = []
        for dst in graph[src]:
            res[src].append(dst)
            res[dst].append(src)

    for src in res.keys():
        res[src] = list(set(res[src]))

    return res



def assert_graphs_equal(a: Graph, b: Graph):
    assert set(a.keys()) == set(b.keys())
    for src in a.keys():
        assert set(a[src]) == set(b[src])


# 1. Empty graph
def test_empty_graph():
    graph = {}
    expected = {}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 2. Single node, no edges
def test_single_node_no_edges():
    graph = {1: []}
    expected = {1: []}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 3. Graph that is already symmetric
def test_already_symmetric():
    graph = {1: [2], 2: [1]}
    expected = {1: [2], 2: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 4. Simple one-way link
def test_simple_asymmetric():
    graph = {1: [2], 2: []}
    expected = {1: [2], 2: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 5. Missing node key for the destination (implicit nodes)
def test_missing_destination_key():
    graph = {1: [2]}  # Node 2 is not in keys
    expected = {1: [2], 2: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 6. Graph with self-loops
def test_self_loop():
    graph = {1: [1]}
    expected = {1: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 7. Linear chain (A -> B -> C)
def test_chain_graph():
    graph = {1: [2], 2: [3], 3: []}
    expected = {1: [2], 2: [1, 3], 3: [2]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 8. Star graph (one center, multiple leaves)
def test_star_graph():
    graph = {1: [2, 3, 4]}
    expected = {1: [2, 3, 4], 2: [1], 3: [1], 4: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 9. Disjoint subgraphs
def test_disjoint_components():
    graph = {1: [2], 3: [4]}
    expected = {1: [2], 2: [1], 3: [4], 4: [3]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 10. Cyclic directed graph (A -> B -> C -> A)
def test_directed_cycle():
    graph = {1: [2], 2: [3], 3: [1]}
    expected = {1: [2, 3], 2: [1, 3], 3: [1, 2]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 11. Multiple converging links (B -> A, C -> A)
def test_converging_links():
    graph = {1: [], 2: [1], 3: [1]}
    expected = {1: [2, 3], 2: [1], 3: [1]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)

# 12. Complex graph mixed with existing back-links and self-loops
def test_complex_mixed_graph():
    graph = {1: [2, 3], 2: [1, 4], 3: [3], 4: []}
    expected = {1: [2, 3], 2: [1, 4], 3: [1, 3], 4: [2]}
    assert_graphs_equal(get_symmetric_graph(graph), expected)





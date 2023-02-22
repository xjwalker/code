"""
Consider an undirected graph where each edge weighs 6 units. Each of the nodes is labeled consecutively from 1 to n.

You will be given a number of queries. For each query, you will be given a list of edges describing an undirected graph.
After you create a representation of the graph, you must determine and report the shortest distance to each of the other
nodes from a given starting position using the breadth-first search algorithm (BFS). Return an array of distances
from the start node in node number order. If a node is unreachable, return -1 for that node.

Example
The following graph is based on the listed inputs:


Key notes:
    - defaultdict(set)
    - deque: due to the ability to pop the left value (FIFO)
    BFS works in a particular way, the neighbors are not processed on the fly,they need to wait that's what the queue is
    for, undirected graphs are very different from regular trees, regular trees have two directions the undirected
    graphs have a list of nodes and this relation needs to be stored in both directions in a dict with the value being
    the list of the nodes.


"""

from collections import defaultdict, deque


def get_graph(edges):
    graph = defaultdict(set)
    for v1, v2 in edges:
        graph[v1].add(v2)
        graph[v2].add(v1)
    return graph


def bread_first_search(n, m, edges, s):
    """
    :param n: amount of nodes?
    :param m: ??
    :param edges: relations between nodes
    :param s: starting position.
    :return: list with the distances between the neighboors
    """
    graph = get_graph(edges)
    queue = deque([s])
    print(queue)
    visited = {s}
    distances = dict()
    while queue:
        current_node = queue.popleft()
        print(current_node)
        neighbours = graph[current_node]
        print('neighbours ', neighbours)
        print('just visited: ', visited)
        for neighbour in neighbours:
            if neighbour not in visited:
                distances[neighbour] = distances.get(current_node, 0) + 6
                queue.append(neighbour)
                print(neighbour, ' queued')
                visited.add(neighbour)

    res = [distances.get(v2, -1) for v2 in range(1, n + 1) if v2 != s]

    return res


def main():
    res = bread_first_search(4, 2, [[1, 2], [1, 3]], 1)
    print(res)
    assert res == [6, 6, -1]

    res = bread_first_search(3, -1, [[2, 3]], 2)
    print(res)
    assert res == [-1, 6]

    res = bread_first_search(5, -1, [[1, 2], [1, 3], [3, 4]], 1)
    print(res)
    assert res == [6, 6, 12, -1]


if __name__ == '__main__':
    main()

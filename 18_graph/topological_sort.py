from collections import deque


def topological_sort(vertices, edges):
    '''Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.
Given a directed graph, find the topological ordering of its vertices.'''

    sorted_order = []
    if vertices <= 0:
        return sorted_order

    # initialize the graph
    in_degree = {i: 0 for i in range(vertices)}  # count of incoming edges
    graph = {i: [] for i in range(vertices)}  # adjancency list graph

    # build the graph
    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)  # put the child into its parent's list
        in_degree[child] += 1  # increment child's in_degree

    # find all sources, aka all vertices with no in_degrees
    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    # for each source, add it to sorted_order and decrement its children's in_degrees
    # if a child's in_degree becomes zero, add it to sources queue

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(sorted_order) != vertices:
        return []

    return sorted_order


print("Topological sort: " +
      str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
print("Topological sort: " +
      str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
print("Topological sort: " +
      str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4],
                               [3, 0], [3, 1], [3, 2], [4, 1]])))

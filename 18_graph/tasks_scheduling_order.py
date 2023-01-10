from collections import deque


def find_order(tasks, prereqs):
    sorted_order = []
    if tasks <= 0:
        return sorted_order

    graph = {i: [] for i in range(tasks)}
    in_degrees = {i: 0 for i in range(tasks)}

    for prereq in prereqs:
        parent, child = prereq[0], prereq[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    sources = deque()
    for key in graph:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    # if len(sorted_order) != tasks:
    #     return []
    return sorted_order


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()

from collections import deque


def print_orders(tasks, prereqs):
    '''There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a method to print all possible ordering of tasks meeting all prerequisites.'''

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

    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    print_all_sorts(graph, in_degrees, sources, sorted_order)


def print_all_sorts(graph, in_degrees, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)
            sources_for_next_call.remove(vertex)
            for child in graph:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    sources_for_next_call.append(child)

            print_all_sorts(graph, in_degrees,
                            sources_for_next_call, sorted_order)

            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degrees[child] += 1

    if len(sorted_order) == len(in_degrees):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


main()

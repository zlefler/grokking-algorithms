from collections import deque


def is_scheduling_possible(tasks, prereqs):
    '''There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, find out if it is possible to schedule all the tasks.'''

    if tasks <= 0:
        return False

    graph = {i: [] for i in range(tasks)}
    in_degrees = {i: 0 for i in range(tasks)}

    for prereq in prereqs:
        parent, child = prereq[0], prereq[1]
        graph[parent].append(child)
        in_degrees[child] += 1

    array = []
    sources = deque()
    for key in in_degrees:
        if in_degrees[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        array.append(vertex)
        for child in graph[vertex]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                sources.append(child)

    return len(array) == tasks


print("Is scheduling possible: " +
      str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
print("Is scheduling possible: " +
      str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
print("Is scheduling possible: " +
      str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))

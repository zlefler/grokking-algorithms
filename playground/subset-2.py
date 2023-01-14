from collections import deque


def subsets(arr):
    res = []
    queue = deque()
    queue.append([])
    for num in arr:
        length = len(queue)
        for _ in range(length):
            old = queue.popleft()
            for j in range(len(old) + 1):
                new = list(old)
                new.insert(j, num)
                if len(new) == len(arr):
                    res.append(new)
                else:
                    queue.append(new)
    return res


print(subsets([1, 3, 5]))

def subsets(arr):
    subsets = [[]]
    for num in arr:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)


def subsets_with_dupes(arr):
    subsets = [[]]
    current_length = 0
    prev = None
    for num in arr:
        if num == prev:
            n = current_length
        else:
            n = len(arr)
        current_length = 0
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)
            current_length += 1
        prev = num

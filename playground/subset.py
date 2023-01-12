def subsets(arr):
    subsets = [[]]
    for num in arr:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)

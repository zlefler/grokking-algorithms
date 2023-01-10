def find_all(arr: list) -> list:
    '''We are given an unsorted array containing numbers taken from the range 1 to ‘n’. The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.'''
    res = []
    i = 0

    while i < len(arr):
        if arr[i] != i + 1:
            try:
                x = arr.index(arr[i-1])
            except ValueError:
                res.append(i-1)
                i += 1
            else:
                if x < i:
                    res.append(x)
                    i += 1
                else:
                    arr[x], arr[i] = arr[i], arr[x]
        else:
            i += 1
    return res


one = [1, 4, 2, 2]
print(find_all(one))

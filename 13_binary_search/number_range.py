def num_range(arr: list[int], key: int):
    l = 0
    r = len(arr) - 1
    min_valid = float('inf')
    max_valid = -float('inf')
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < key:
            l = mid + 1
        elif arr[mid] > key:
            r = mid - 1
        else:
            min_valid = min(min_valid, mid)
            max_valid = max(max_valid, mid)
    l = 0
    r = max_valid
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] < key:
            if arr[mid - 1] != key:
                break
            else:
                l = mid + 1
        elif arr[mid] == key:
            r = mid - 1
    min_valid = mid
    l = min_valid
    r = len(arr) - 1
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == key:
            l = mid + 1
        elif arr[mid] > key:
            if mid == len(arr) - 1:
                break
            elif arr[mid+1] != key:
                mid += 1
                break
            else:
                r = mid - 1
    max_valid = mid

    return [min_valid, max_valid]


print(num_range([4, 6, 6, 6, 9], 6))

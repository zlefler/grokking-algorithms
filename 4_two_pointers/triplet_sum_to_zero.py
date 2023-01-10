def search_triplets(arr: list) -> list:
    '''Given an array of unsorted numbers, find all unique triplets in it that add up to zero.'''
    arr.sort()
    triplets = []

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        search_pair(arr, -arr[i], i+1, triplets)
    return triplets


def search_pair(arr, target, left, triplets):

    right = len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            triplets.append([-target, arr[left], arr[right]])
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target > current:
            left += 1
        else:
            right -= 1

    # left = 0
    # right = len(arr) - 1

    # while left + 1 < right:
    #     x = arr[left] + arr[left + 1] + arr[right]
    #     if x == 0:
    #         triplets.append([arr[left], arr[left + 1], arr[right]])
    #     elif x > 0:
    #         left += 1
    #         continue

    #     y = arr[left] + arr[right - 1] + arr[right]
    #     if y == 0:
    #         triplets.append([arr[left], arr[right - 1], arr[right]])
    #         right -= 1
    #     elif x > 0:
    #         right -= 1
    #     else:
    #         left += 1

    # return triplets


one = [-3, 0, 1, 2, -1, 1, -2]
# two = [-5, 2, -1, -2, 3]

print(search_triplets(one))

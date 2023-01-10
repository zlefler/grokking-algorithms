def target_sum(arr, k):
    arr.sort()
    left = 0
    triplets = []
    while left < len(arr) - 2:
        if left > 0 and arr[left] == arr[left-1]:
            left += 1
        else:
            triplet = find_pair(arr, left + 1, -arr[left])
            if triplet:
                triplets.append([arr[left], triplet[0], triplet[1]])
            left += 1
    return triplets


def find_pair(arr, i, target):
    left = i
    right = len(arr) - 1
    while right > left:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target:
            left += 1
        else:
            right -= 1


arr1 = [-3, 0, 1, 2, -1, 1, -2]
arr2 = [-5, 2, -1, -2, 3]

print(target_sum(arr1, 0))
print(target_sum(arr2, 0))

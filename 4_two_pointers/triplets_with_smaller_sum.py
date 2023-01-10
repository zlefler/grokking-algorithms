from cgitb import small


def smaller_sum(arr: list, target: int) -> int:
    '''Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.'''

    arr.sort()
    count = 0

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while right > left:
            sum = arr[i] + arr[left] + arr[right]
            if sum < target:
                count += right - left
                left += 1
            else:
                right -= 1

    return count


arr1 = [-1, 0, 2, 3]
targ1 = 3
arr2 = [-1, 4, 2, 1, 3]
targ2 = 5

print(smaller_sum(arr1, targ1))
print(smaller_sum(arr2, targ2))

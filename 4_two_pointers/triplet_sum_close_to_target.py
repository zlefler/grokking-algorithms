def close_to_target(arr: list, target: int) -> int:
    '''Given an array of unsorted numbers and a target number, find a triplet in the array 
    whose sum is as close to the target number as possible, return the sum of the triplet. 
    If there are more than one such triplet, return the sum of the triplet with the smallest sum.'''
    arr.sort()
    closest_distance = float('inf')
    for i in range(len(arr)-2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            target_diff = target - arr[i] - arr[left] - arr[right]
            if target_diff == 0:
                return target
            if abs(target_diff) < abs(closest_distance) or (abs(target_diff) == abs(closest_distance) and target_diff > closest_distance):
                closest_distance = target_diff
            if target_diff > 0:
                left += 1
            else:
                right -= 1
    return target - closest_distance


    # arr.sort()
    # left, right = 0, len(arr) - 1
    # closest = float('inf')
    # closest_distance = float('inf')
    # while left < right:
    #     x = arr[left] + arr[left + 1] + arr[right]
    #     if x == target:
    #         return x
    #     distance = min(abs(x - target), abs(target - x))
    #     if distance < closest_distance:
    #         closest_distance = distance
    #         closest = x
    #     elif distance == closest_distance and x < closest:
    #         closest = x
    #     elif x < target:
    #         x = arr[left] + arr[right - 1] + arr[right]
    #         if x == target:
    #             return x
    #         distance = min(abs(x - target), abs(target - x))
    #         if distance < closest_distance:
    #             closest_distance = distance
    #             closest = x
    #         elif distance == closest_distance and x < closest:
    #             closest_distance = distance
    #             closest = x
    #         elif x < target:
    #             left += 1
    #         else:
    #             right -= 1
    #     else:
    #         right -= 1
    # return closest
    # sort array
    # left = 0
    # right = array - 1
    # compare left + left+1 + right
    # if low, compare left + right-1 + right
    # if low, left += 1
    # if high, right -= 1
    # if on, return
one_array = [-2, 0, 1, 2]
one_target = 2
two_array = [-3, -1, 1, 2]
two_target = 1
three_array = [0, 0, 1, 1, 2, 6]
three_target = 5

print(close_to_target(one_array, one_target))
print(close_to_target(two_array, two_target))
print(close_to_target(three_array, three_target))

from turtle import end_fill


def find_max(array: list[int]) -> int:

    # This one isn't hard no matter how you do it, but the trick for max efficiency is that
    # your left and right pointers will always land on the right answer.
    '''Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].'''

    start = 0
    end = len(array) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if array[mid - 1] < array[mid]:
            if array[mid + 1] < array[mid]:
                return array[mid]
            start = mid + 1
        else:
            end = mid - 1

    # start, end
    # while end > start
    # if mid - 1 > mid > mid + 1:
    #     r = mid - 1
    # if mid - 1 < mid < mid + 1
    #     l = mid + 1
    # if mid - 1 < mid and mid + 1 < mid:
    #     return mid


print(find_max([1, 3, 8, 12, 4, 2]))

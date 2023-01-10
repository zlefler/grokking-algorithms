def insert_interval(intervals, new_interval):
    '''Given a list of non-overlapping intervals sorted by their start time, insert a given interval at the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.'''

    i = 0
    for i in range(len(intervals)):
        if intervals[i][0] > new_interval[0]:
            intervals.insert(i, new_interval)
            break

    # intervals.append(new_interval)
    # intervals.sort(key = lambda x: x[0])

    start = intervals[0][0]
    end = intervals[0][1]

    merged = []

    for interval in intervals:
        if interval[0] <= end:
            end = max(end, interval[1])
        else:
            merged.append((start, end))
            start = interval[0]
            end = interval[1]
    merged.append((start, end))

    return merged

    # insert interval correctly
    #     if can use built-in sort:
    #         append new interval
    #         resort list
    #     else:
    #         iterate through list
    #         when hit larger start time, insert new at i - 1

    # merge intervals
    #     set start and end to first interval's
    #     iterate through list
    #     if new start <= old end, update end to new end
    #     else append interval to merge_list, set new start and end to current interval's


print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 6]))
print(insert_interval([[1, 3], [5, 7], [8, 12]], [4, 10]))
print(insert_interval([[2, 3], [5, 7]], [1, 4]))

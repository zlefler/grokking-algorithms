def merge_intervals(intervals):

    intervals.sort(key=lambda x: x[0])

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

    total = 0

    for interval in merged:
        total += interval[1] - interval[0]

    return total

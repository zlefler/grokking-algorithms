class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals: list) -> list:
    '''Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.'''
    if len(intervals) < 2:
        return intervals

    intervals.sort(key=lambda x: x.start)

    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(interval.end, end)
        else:
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    merged_intervals.append(Interval(start, end))
    return merged_intervals


arr1 = [[6, 7], [2, 4], [5, 9]]
arr2 = [[1, 4], [2, 6], [3, 5]]

print("Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
    i.print_interval()
print()

print("Merged intervals: ", end='')
for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
    i.print_interval()
print()

print("Merged intervals: ", end='')
for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
    i.print_interval()
print()

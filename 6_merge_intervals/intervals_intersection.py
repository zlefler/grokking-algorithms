# Check to see if one start time falls in the interval of the other (try both ways).
# If it does, append it to the merge list.
# Either way, afterwards, increment whichever list's current interval has the earlier end time.

def merge(arr1, arr2):
    '''Given two lists of intervals, find the intersection of these two lists. 
    Each list consists of disjoint intervals sorted on their start time.'''

    res = []

    i, j, start, end = 0, 0, 0, 1

    while i < len(arr1) and j < len(arr2):
        a_overlaps_b = arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end]

        b_overlaps_a = arr2[j][start] >= arr1[i][start] and arr2[j][start] <= arr1[i][end]

        if (a_overlaps_b or b_overlaps_a):
            res.append([max(arr1[i][start], arr2[j][start]),
                       min(arr1[i][end], arr2[j][end])])

        if arr1[i][end] < arr2[j][end]:
            i += 1
        else:
            j += 1

    return res


def main():
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " +
          str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()

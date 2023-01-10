from collections import deque
from heapq import *


class Meeting:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.end < other.end


def min_meeting_rooms(meetings: list[list[int]]) -> int:
    min_rooms = 0
    intersecting = deque()
    meetings.sort(key=lambda a: a[0])

    for current_meeting in meetings:
        while intersecting:
            if current_meeting[0] < intersecting[0][1]:
                break
            else:
                intersecting.popleft()
        intersecting.append(current_meeting)
        min_rooms = max(min_rooms, len(intersecting))

    return min_rooms


def main():
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
    print("Minimum meeting rooms required: " +
          str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
    print("Minimum meeting rooms required: " + str(min_meeting_rooms(
        [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))

# sort meetings by start time
# see if next meeting start < last meeting end
# add intersecting meetings to list (stack)
# when add meeting, min_rooms = with max(min_rooms, len(intersecting))
# with new meeting, if items in intersecting, go through and see which still intersect
# add and subtract from list as needed

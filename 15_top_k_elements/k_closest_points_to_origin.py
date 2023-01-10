from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return (self.x ** 2) + (self.y ** 2)

    def print_point(self):
        print(f'[{str(self.x)},{str(self.y)}] ', end='')


def find_closest_points(points, k):
    '''Given an array of points in a 2D plane, find ‘K’ closest points to the origin.'''
# Not in the problem explanation, but:
# The Euclidean distance of a point P(x,y) from the origin can be calculated
# # through the following formula: sqrt((x ** 2) + (y ** 2)).
    maxHeap = []

    for i in range(k):
        heappush(maxHeap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() < maxHeap[0].distance_from_origin():
            heappop(maxHeap)
            heappush(maxHeap, points[i])

    return maxHeap


result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
print("Here are the k points closest the origin: ", end='')
for point in result:
    point.print_point()

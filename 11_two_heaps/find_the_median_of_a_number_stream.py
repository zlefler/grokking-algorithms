from heapq import *

'''Design a class to calculate the median of a number stream. The class should have the following two methods:

insertNum(int num): stores the number in the class
findMedian(): returns the median of all numbers inserted in the class
If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

'''

# heapq always makes a minHeap. So to make a maxHeap, you push the negative version of the number to the heap,
# and pop the negative as well.
# When trying to find the median, if both heaps are even, take the top numbers, add together and
# divide by two. If one heap is bigger, just return that number as-is.


class MedianOfAStream():
    # holds the smallest numbers
    maxHeap = []
    # holds the biggest numbers
    minHeap = []

    def insert_num(self, num: int):
        # if max is empty or max already has larger numbers than this, put it in there
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        # arbitrarily pick one heap to be the larger if odd, sort if off by more than that
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def find_median(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0

        return -self.maxHeap[0] / 1.0


medianOfAStream = MedianOfAStream()
medianOfAStream.insert_num(3)
medianOfAStream.insert_num(1)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(5)
print("The median is: " + str(medianOfAStream.find_median()))
medianOfAStream.insert_num(4)
print("The median is: " + str(medianOfAStream.find_median()))

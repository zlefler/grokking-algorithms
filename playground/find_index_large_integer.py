# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    def __init__(self, array):
        self.array = array

    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        ans = sum(self.array[l:r+1]) - sum(self.array[x:y+1])
        if ans > 0:
            return 1
        elif ans < 0:
            return -1
        else:
            return 0

    def length(self) -> int:
        return len(self.array)


class Solution:
    def getIndex(self, reader):
        left = 0
        length = reader.length()
        while (length > 1):
            length //= 2
            cmp = reader.compareSub(left, left + length - 1, left + length,
                                    left + length + length - 1)
            if cmp == 0:
                return left + length + length
            if cmp < 0:
                left += length
        return left


array = [7, 7, 7, 7, 10, 7, 7, 7]
# def getIndex(self, reader) -> int:
#     y = reader.length() - 1
#     l = 0
#     while True:
#         shortened = None
#         mid = (y + l - 1) // 2
#         r = mid
#         x = mid+1
#         if r-l > y-x:
#             if l == 0:
#                 y -= 1
#                 shortened = 'right'
#             else:
#                 l -= 1
#         elif r-l < y-x:
#             if y == reader.length() - 1:
#                 l += 1
#                 shortened = 'left'
#             else:
#                 y += 1
#         # print(l, r, x, y)
#         ans = reader.compareSub(l, r, x, y)
#         if ans == 1:
#             if r - l == 0:
#                 return l
#             y = mid
#         elif ans == -1:
#             if y - x == 0:
#                 return x
#             l = mid
#         else:
#             if shortened == 'right':
#                 return reader.length() - 1
#             elif shortened == 'left':
#                 return 0
#             else:
#                 raise Exception('no shortening, still equal sides')


arr2 = [6, 6, 12]
reader = ArrayReader(array)
ans = Solution()
print(ans.getIndex(reader))


# mid = y // 2
# reader(0, mid, mid+1, length)
# if 1: y = mid
# if -1: l = mid+1
# add check if r-l or y-x = 0:
# if so return larger
# if 0, raise error

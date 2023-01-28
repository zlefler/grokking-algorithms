from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        queue = deque()
        queue.append('()')
        while queue:
            length = len(queue)
            for _ in range(length):
                old = queue.popleft()
                print(old)
                for j in range((len(old) // 2) + 1):
                    new = str(old)
                    if j == len(new):
                        new = new[j:] + '()'
                    else:
                        new = new[:j] + '()' + new[j+1:]
                    if len(new) == n*2:
                        ans.append(new)
                    else:
                        queue.append(new)

                        

sol = Solution()

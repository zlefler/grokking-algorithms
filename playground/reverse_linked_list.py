class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if (not head) or (not head.next):
            return head
        h = head.val
        p = self.reverseList(head.next)
        pval = p.val
        head.next.next = head
        hnn = head.val
        head.next = None
        return p


h1 = ListNode(1)
h1.next = ListNode(2)
h1.next.next = ListNode(3)
h1.next.next.next = ListNode(4)
h1.next.next.next.next = ListNode(5)

sol = Solution()
print(sol.reverseList(h1))

# 5 -> 4 -> x -> 4

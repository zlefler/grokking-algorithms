class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        curr = self
        print(curr.val)
        while curr.next:
            curr = curr.next
            print(curr.val)


def remove_nth_node_from_end(head, n):
    if not head.next:
        return None

    i = 0  # 4
    curr = head  # 4
    while curr.next:
        curr = curr.next
        i += 1

    curr = head
    prev = None

    for _ in range(i - (n-1)):
        prev = curr
        curr = curr.next

    if n == 1:
        prev.next = None
    else:
        prev.next = curr.next

    return head


n1 = Node(1)
n1.next = Node(2)
n1.next.next = Node(3)
n1.next.next.next = Node(4)
n1.next.next.next.next = Node(5)

remove_nth_node_from_end(n1, 2)
n1.print()

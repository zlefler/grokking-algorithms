class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def middle_of_list(head: Node) -> int:
    fast, slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    return slow


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Middle Node: " + str(middle_of_list(head).value))

head.next.next.next.next.next = Node(6)
print("Middle Node: " + str(middle_of_list(head).value))

head.next.next.next.next.next.next = Node(7)
print("Middle Node: " + str(middle_of_list(head).value))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


def reverse_sub_list(head, p, q):
    '''Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.'''
    if p == q:
        return head

    curr, prev = head, None
    i = 0
    while curr is not None and i < p - 1:
        prev = curr
        curr = curr.next
        i += 1

    last_node_of_first_part = prev
    last_node_of_sub_list = curr

    next = None
    i = 0

    while curr is not None and i < q - (p + 1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i += 1

    if last_node_of_first_part is not None:
        last_node_of_first_part.next = prev
    else:
        head = prev

    last_node_of_sub_list.next = curr
    return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_sub_list(head, 2, 4)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()

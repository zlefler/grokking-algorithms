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


def reverse_every_k_elements(head, k):
    '''Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.
If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.'''

    if k <= 1 or head is None:
        return head

    curr, prev = head, None

    while True:
        last_node_of_prev = prev
        last_node_of_sub_list = curr
        next = None
        i = 0

        while curr is not None and i < k:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            i += 1

        if last_node_of_prev is not None:
            last_node_of_prev.next = prev
        else:
            head = prev

        last_node_of_sub_list.next = curr

        if curr is None:
            break
        prev = last_node_of_sub_list

    return head

    # doesn't work:
    # curr = head
    # prev = None
    # i = 0
    # next = None
    # while curr is not None:
    #     last_node_of_current = curr
    #     while i < k:
    #         next = curr.next
    #         curr.next = prev
    #         prev = curr
    #         curr = next
    #     # first_node_of_previous = curr
    #     last_node_of_current.next = curr
    # last_node_of_current.next = curr
    # return head


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

print("Nodes of original LinkedList are: ", end='')
head.print_list()
result = reverse_every_k_elements(head, 3)
print("Nodes of reversed LinkedList are: ", end='')
result.print_list()

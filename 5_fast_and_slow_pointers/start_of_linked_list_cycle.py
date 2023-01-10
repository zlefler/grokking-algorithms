class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


def find_cycle_start(head):
    cycle_length = 0
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    current = slow
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        if current == slow:
            break
    return cycle_length


def find_start(head, cycle_length):
    p1, p2 = head, head
    # move p2 ahead by the cycle length amount
    while cycle_length > 0:
        p2 = p2.next
        cycle_length -= 1
    # then wherever they meet is the start of the cycle
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = head.next.next
print("LinkedList cycle starts: " + str(find_cycle_start(head)))
head.next.next.next.next.next.next = head.next.next.next
print("LinkedList cycle starts: " + str(find_cycle_start(head)))

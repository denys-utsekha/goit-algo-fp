
from linked_list import LinkedList, print_list, Node

llist = LinkedList()

llist.insert(20)
llist.insert(25)
llist.insert(10)
llist.insert(5)
llist.insert(15)

print("Original list:")
print_list(llist.head)


def merge_sort(head):
    if head is None or head.next is None:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left_half = merge_sort(head)
    right_half = merge_sort(next_to_middle)

    sorted_list = merge(left_half, right_half)
    return sorted_list


def get_middle(head):
    if head is None:
        return head

    slow_ptr = head
    fast_ptr = head

    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr


def merge(left, right):
    dummy_node = Node()
    current_node = dummy_node

    while left is not None and right is not None:
        if left.data < right.data:
            current_node.next = left
            left = left.next
        else:
            current_node.next = right
            right = right.next

        current_node = current_node.next

    if left is not None:
        current_node.next = left
    elif right is not None:
        current_node.next = right

    return dummy_node.next


print("Sorted list:")
print_list(merge_sort(llist.head))

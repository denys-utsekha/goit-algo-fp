
from linked_list import LinkedList, print_list, Node

llist1 = LinkedList()
llist1.insert(1)
llist1.insert(3)
llist1.insert(5)

llist2 = LinkedList()
llist2.insert(2)
llist2.insert(4)
llist2.insert(6)


def merge_sorted_lists(head1, head2):
    dummy_node = Node()
    current_node = dummy_node

    while head1 is not None and head2 is not None:
        if head1.data <= head2.data:
            current_node.next = head1
            head1 = head1.next
        else:
            current_node.next = head2
            head2 = head2.next

        current_node = current_node.next

    if head1 is not None:
        current_node.next = head1

    if head2 is not None:
        current_node.next = head2

    return dummy_node.next


print("Merged list:")
print_list(merge_sorted_lists(llist1.head, llist2.head))

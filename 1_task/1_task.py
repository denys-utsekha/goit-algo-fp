
from linked_list import LinkedList, print_list

llist = LinkedList()

llist.insert(20)
llist.insert(25)
llist.insert(10)
llist.insert(5)
llist.insert(15)

print("Original list:")
print_list(llist.head)


def reverse(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head


print("Reversed list:")
print_list(reverse(llist.head))

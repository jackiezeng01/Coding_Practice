from linked_list_implementation import Node
from linked_list_implementation import LinkedList

''' Implement an algorithm to find the kth to last element of a singly linked list. 

    # Clarify with interviewer what is considered the last element. I implemented the iterative and recursive differently. One counts the last node as the end, and the other counts the Null as the end.
'''

def return_kth_to_last_iterative(n, k):
    # Two pointers spaced k apart
    p1 = n
    p2 = n

    # Move p2 k steps into the linked list
    for i in range(k):
        if p2 is None: return None
        else: p2 = p2.next

    # Traverse the linked list with the two pointers until p2 hits the end. p1 is then our kth to last element
    while p2.next is not None:
        p1 = p1.next
        p2 = p2.next
    
    return p1

def print_kth_to_last_recursive(n, k):
    # Base case
    if n == None:
        return 0
    print(n.val)
    # Once the pointer reaches the end, it passes back a counter 0. The parent functions each increment by 1 to the index
    index = print_kth_to_last_recursive(n.next, k) + 1
    # If we're at the right node
    if (index == k):
        print("The kth to last node is ", n.val)
    return index

if __name__ == "__main__":
    l = LinkedList()
    l.append(0)
    l.append(1)
    l.append(2)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.append(7)
    l.append(8)
    l.append(9)

    kth_to_last = return_kth_to_last_iterative(l.head, 3)
    print(kth_to_last.val)

    print_kth_to_last_recursive(l.head, 3)

    # l.print_list()

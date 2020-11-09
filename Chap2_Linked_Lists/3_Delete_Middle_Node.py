from linked_list_implementation import Node
from linked_list_implementation import LinkedList

'''
Implement an algorithm to delete a node in the middle (i.e. any node thats not the first and last node) of a singly linked list, given only access to that node.
'''

def delete_middle_node(n):
    ''' Store the value of the next node in n, and then delete the next node
    '''
    if n.next:
        # Store n.next values in n
        n.val = n.next.val
        # Delete n.next
        n.next = n.next.next



if __name__ == "__main__":
    l = LinkedList()
    l.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    l.head.next = second
    second.next = third
    third.next = fourth

    delete_middle_node(second)

    l.print_list()

from linked_list_implementation import Node
from linked_list_implementation import LinkedList

''' Write code to remove duplicates from an unsorted linked list. 
    
    Clarification: do we want to remove the duplicates that are not the first appearance?
'''

def remove_dups(n):
    '''
    Inputs: n = head of the linked list
    '''
    # Make set, traverse the linked list, and if there is a duplicate, remove it
    elem_set= set()

    # Make fake first node, this acts as the previous node to the one we're checking. We need this because this is a singly linked list and we cannot go back to change the previous counter. 
    previous = Node(None)

    curr = n
    while curr is not None:
        # If value at current node is in dict, this node is a duplicate and we must remove it from the linked list
        if curr.val in elem_set:
            previous.next = curr.next
        # If value at current node not in dict, add it to the dict. Also increment previous
        else:
            elem_set.add(curr.val)
            previous = curr
        curr = curr.next 

def remove_dups_no_buffer(n):
    ''' O(n^2) time complexity, O(1) space complexity
    '''
    curr = n
    # Have 2 pointers, one of them is a runner. For each node, we check all the following nodes and delete duplicate nodes
    while curr is not None:
        # Runner pointer
        runner = curr
        # We care about runner.next because if we traverse we cannot delete an element bc singly linked list
        while runner.next is not None:
            # If node at runner is duplicate, delete it
            if runner.next.val == curr.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next
    return

if __name__ == "__main__":
    l = LinkedList()
    l.append(5)
    l.append(2)
    l.append(0)
    l.append(2)
    l.append(3)
    l.append(3)
    l.append(3)
    l.append(4)

    # remove_dups(l.head)
    remove_dups_no_buffer(l.head)


    l.print_list()

    

'''
Sort a linked list that contains just 0s and 1s. That is, modify the list such that all 0s come before all 1s
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, val):
        newnode = Node(val)
        # if node in front
        if val < self.head.data:
            newnode.next = self.head
            self.head = newnode
            return
        curr = self.head
        # node somewhere in the middle
        while curr.next != None:
            if val >= curr.data and val <= curr.next.data:
                newnode.next = curr.next
                curr.next = newnode
                return
            curr = curr.next
        # node at end
        curr.next = newnode

def print_list(head):
    curr = head
    while curr != None:
        print(curr.data)
        curr = curr.next

def sort_ll(head):
    l0, l1 = LinkedList(), LinkedList()
    l0.head, l1.head = Node(None), Node(None)
    p0, p1 = l0.head, l1.head
    
    # traverse linked list, and put node in the right list
    curr = head
    while curr != None:
        if curr.data == 0:
            p0.next = curr
            p0 = curr
        else:
            p1.next = curr
            p1 = curr

        curr = curr.next
    
    # connect two pieces
    p0.next = l1.head.next

    return l0.head.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.head = Node(0)
    ll.insert(0)
    ll.insert(1)
    ll.insert(0)
    ll.insert(1)
    ll.insert(1)
    ll.insert(0)

    res = sort_ll(ll.head)

    print_list(res)

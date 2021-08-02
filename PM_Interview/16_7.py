'''
Insert a node into a sorted linked list (in order). Don't forget about what happens when the new element is at the start or end.
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, node) -> None:
        self.head = node

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

    def print_list(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

    
    
if __name__ == "__main__":
    head = Node(5)
    ll = LinkedList(head)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(7)

    ll.print_list()

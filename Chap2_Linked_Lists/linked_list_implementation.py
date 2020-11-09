# Implement a linked list

class Node:

    def __init__(self, data):
        self.val = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0


    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.val)
            curr = curr.next


    def append(self, data):
        '''O(1)
        '''
        # Create new node
        new_node = Node(data)

        # If linked list is empty, set new element as the head
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return

        # Set the pointer of the tail to the appended node
        self.tail.next = new_node
        # Set the tail node to be the new node
        self.tail = new_node
        # Increment length of linked list
        self.length += 1


    def prepend(self, data):
        ''' O(1)
        '''
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        
        new_node.next = self.head
        self.head = new_node
        # if self.head is not None:

        self.length += 1

    
    def insert(self, index, data):
        '''O(n)
        '''
        # Check params
        if index >= self.length-1:
            return self.append(data)

        # Make new node
        new_node = Node(data)
        # Pointer to current node
        curr = self.head
        # index for the while loop
        i = 0
        # Traverse to node right before the index we want to add
        while curr:
            if i+1 == index:
                # Set pointer of new node to the element after the new node
                new_node.next = curr.next
                # Set pointer of current node to new node
                curr.next = new_node
                self.length += 1
                return
            index += 1


    def remove_at_index(self, index):
        # Check params
        # Empty list
        if self.head == None:
            return
        # If index = 0, we remove head
        if index == 0:
            self.head = self.head.next
            return
        # If index >= length, return
        if index >= self.length:
            return 
        
        prev = self.head
        # Find previous node of the node that needs to be deleted
        for i in range(index-1):
            prev = prev.next
            if prev is None:
                break
        
        # Need this if linked list doesn't have built in length
        if prev is None:
            return
        if prev.next is None:
            return

        # Store pointer for the next of the node that will be deleted
        next = prev.next.next
        # Unlink node
        prev.next = None
        # Link node to the node after the deleted node
        prev.next = next

if __name__ == "__main__":
    l = LinkedList()
    l.append(5)
    l.append(2)
    l.append(0)
    # l.prepend("1")
    # l.insert(1, "2")
    # l.insert(0, "zero")
    # l.insert(222, "too big")
    l.remove_at_index(2)
    l.print_list()
    # print("length:", l.length)


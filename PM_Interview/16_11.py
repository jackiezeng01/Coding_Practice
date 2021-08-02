'''
Write a function to check if two queues are identical (same values in the same order). It is okay to modify / destroy the 2 queues
'''

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self,val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next = newnode
            self.tail = newnode
        self.length += 1

    def dequeue(self):
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def print(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

def is_identical(q1, q2):
    if q1.length != q2.length:
        return False
    while q1.length != 0:
        n1, n2 = q1.dequeue(), q2.dequeue()
        if n1.data != n2.data:
            return False
    return True


if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.enqueue(5)
    q1.print()
    print("_______")

    q2 = Queue()
    q2.enqueue(1)
    q2.enqueue(2)
    q2.enqueue(3)
    q2.enqueue(4)
    q2.enqueue(5)
    q2.print()
    print("_______")


    res = is_identical(q1, q2)
    print(res)
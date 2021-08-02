'''
Write a function to remove the 13th element from a queue (but keep all the other elems in place and in the same order)
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
    
def remove_nth(q, n):
    # if we remove and add in the same order, we would get the same queue
    counter = 1
    for i in range(0, q.length):
        temp = q.dequeue()
        if counter != n:
            q.enqueue(temp.data)
        counter += 1
    return q    

if __name__ == "__main__":
    q1 = Queue()
    q1.enqueue(1)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)
    q1.enqueue(5)
    q1.print()
    print("_______")


    res = remove_nth(q1, 3)
    res.print()
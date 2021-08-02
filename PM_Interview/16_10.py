'''
Write a function that removes all the even numbers from a stack. 
You should return the original stack, not the new one.
''' 

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class Stack:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self,val):
        newnode = Node(val)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
        self.length += 1

    def pop(self):
        removed = self.head
        self.head = self.head.next
        self.length -= 1
        return removed
    
    def print(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next

def remove_even_nums(stack):
    temp = Stack()

    while stack.length != 0:
        elem = stack.pop()
        # if odd, put in temp stack, we don't care about evens
        if elem.data%2 == 1:
            temp.push(elem.data)
    
    # put elems in temp stack back to orig stack
    while temp.length != 0:
        elem = temp.pop()
        stack.push(elem.data)
    
    return stack


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(6)
    stack.push(7)

    stack.print()
    print("_______")

    res = remove_even_nums(stack)

    res.print()
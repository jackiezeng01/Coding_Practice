'''
Write a function that takes a stack as input and returns a new stack which has the elements reverse
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


def reverse_stack(stack):
    res = Stack()

    while stack.length != 0:
        node = stack.pop()
        res.push(node.data)

    return res


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

    res = reverse_stack(stack)

    res.print()
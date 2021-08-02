'''
Insert an element into a binary search tree (in order). You may assume that the binary search tree contains integers
'''

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data

    def insert(self, val):
        if val < self.data: # smaller than curr elem
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else: # bigger or equal to curr elem
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

            
if __name__ == "__main__":
    n1 = Node(5)
    n1.insert(2)
    n1.insert(3)
    n1.insert(7)
    n1.print_tree()
       


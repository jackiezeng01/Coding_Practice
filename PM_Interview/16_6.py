'''
Given a binary search tree with all integers as values, find the sum of the tree
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

def treesum(root):
    if root == None:
        return 0
    return (root.data + treesum(root.left) + 
            treesum(root.right))

if __name__ == "__main__":
    n1 = Node(5)
    n1.insert(2)
    n1.insert(3)
    n1.insert(7)
    # n1.print_tree()

    res = treesum(n1)
    print(res)
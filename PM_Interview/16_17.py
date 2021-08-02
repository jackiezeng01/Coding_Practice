'''
Using depth first search, check if a tree contains a value.

DFS psuedocode:

void DFS(root):
    if (root == None)
        return
    visit(root)
    root.visited = True
    for each (Node n in root.adjacent):
        if (n.visted == false){
            DFS(n)
        }

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

def DFS(root, x):
    visited = set()
    return DFS_util(root, x, visited)

def DFS_util(root, x, visited):
    visited.add(root)
    if root == None:
        return False
    if root.data == x:
        return True
    if root.left and root.left not in visited:
        return DFS_util(root.left, x, visited)
    if root.right and root.right not in visited:
        return DFS_util(root.right, x, visited)

if __name__ == "__main__":
    n1 = Node(5)
    n1.insert(2)
    n1.insert(3)
    n1.insert(7)

    res = DFS(n1, 2)
    print(res.data)


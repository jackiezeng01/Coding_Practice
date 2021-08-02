from collections import deque

'''
Write the psuedocode for BFS on a binray tree. Try to be as detailed as possible

def BFS(root):
    Queue queue = new Queue()
    root.marked = True
    queue.enqueue(root);

    while (queue is not empty):
        node r = queue.dequue
        visit(r)
        for each neighbor of r:
            if not marked, mark and add to queue
'''

class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data
        self.visited = False

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

def BFS(root, x):
    q = deque()
    root.visited = True
    q.append(root)

    while q:
        elem = q.popleft()
        if elem.data == x:
            return True
        # enqueue all unvisited neighbors
        if root.left: 
            q.append(root.left)
        if root.right: 
            q.append(root.right)
    return False

if __name__ == "__main__":
    n1 = Node(5)
    n1.insert(2)
    n1.insert(3)
    n1.insert(7)

    res = BFS(n1, 2)
    print(res)


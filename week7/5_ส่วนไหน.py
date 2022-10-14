class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        a=Node(data)
        if self.root is None:
            self.root = a
            return self.root
        else:
            t = self.root
            while True:
                if data <= t.data:
                    if t.left == None:
                        t.left = a
                        return self.root
                    else:t=t.left
                else:
                    if t.right == None:
                        t.right = Node(data)
                        return self.root
                    else:t=t.right
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self,k):
        t = self.root
        while True:
            if k == t.data:
                if t == self.root:return print("Root")
                elif t.left == None and t.right == None:return print("Leaf")
                else:return print("Inner")
            elif k < t.data:
                if t.left == None:
                    return print("Not exist")
                else:t=t.left
            else:
                if t.right == None:
                    return print("Not exist")
                else:t=t.right
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])
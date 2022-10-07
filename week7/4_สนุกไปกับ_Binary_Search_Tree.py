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

    def preOrder(self,node):
        if node!=None:
            print("",node,end="")
            self.preOrder(node.left)
            self.preOrder(node.right)
    
    def inOrder(self,node):
        if node!=None:
            self.inOrder(node.left)
            print("",node,end="")
            self.inOrder(node.right)

    def postOrder(self,node):
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print("",node,end="")
    
    def bfs(self,node,q = []):
        if node != None:
            print("",node,end="")
            if node.left!=None:q.append(node.left)
            if node.right!=None:q.append(node.right)
            if len(q)!=0:self.bfs(q.pop(0),q)
            else:return
    
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Preorder :",end="")
T.preOrder(root)
print("\nInorder :",end="")
T.inOrder(root)
print("\nPostorder :",end="")
T.postOrder(root)
print("\nBreadth :",end="")
T.bfs(root)
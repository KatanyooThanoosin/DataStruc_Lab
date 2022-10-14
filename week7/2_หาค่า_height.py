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
        a = Node(data)
        if self.root is None :
            self.root = a 
            return self.root
        else :
            t = self.root 
            while True :
                if data <= t.data :
                    if t.left == None :
                        t.left = a 
                        return self.root
                    else :
                        t = t.left
                else :
                    if t.right == None :
                        t.right = a
                        return self.root
                    else :
                        t = t.right    
    
    def height(self, node):
        if node is not None :
            return max(self.height(node.left),self.height(node.right))+1
        else:
            return -1
            
T = BST()
inp = [int(i) for i in input("Enter Input : ").split()]
for i in inp:T.insert(i)
print("Height of this tree is :",T.height(T.root))
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        return str(self.val)
  
class AVL_Tree(object): 
    def __init__(self):
        self.root = None
    
    def changeHeight(self,a):
        if a!=None:
            a.height = max(self.changeHeight(a.left),self.changeHeight(a.right))+1
            return a.height
        else:
            return -1
    
    def insert(self,node,data):
        if self.root is None:
            self.root = TreeNode(data)
            return self.root
        else:
            if node != None:
                if data <= node.val:
                    node.left = self.insert(node.left,data)
                else:
                    node.right = self.insert(node.right,data)
            else:
                return TreeNode(data)
            
            l = node.left.height if node.left is not None else -1
            r = node.right.height if node.right is not None else -1
            if abs(l-r)>1:
                a = self.root
                if l>r:
                    if data<=node.left.val:
                        a = ll(node)
                    else:
                        node.left = rr(node.left)
                        node = ll(node)
                        a = node
                else:
                    if data<=node.right.val:
                        node.right = ll(node.right)
                        node = rr(node)
                        a = node
                    else:
                        a = rr(node)
                changeHeight(a)
                return a
            else:
                node.height = max(l,r)+1
                return node
def rr(px):
    py = px.right
    px.right = py.left
    py.left = px
    return py
    
def ll(px):
    py = px.left
    px.left = py.right
    py.right = px
    return py

def changeHeight(a):
    if a!=None:
        a.height = max(changeHeight(a.left),changeHeight(a.right))+1
        return a.height
    else:
        return -1

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def fillData(node, data,k,count = 1,q=[]):
    if count > int(k/2):
        node.val = data.pop(0)
    if node.left:q.append(node.left)
    if node.right:q.append(node.right)
    if len(q)>0:fillData(q.pop(0),data,k,count+1,q)

def cutting(node):
    if node.left != None and node.right != None:
        cutting(node.left)
        cutting(node.right)
        node.val = min(node.left.val,node.right.val)
        node.left.val -= node.val
        node.right.val -= node.val

def sumTree(node):
    if node!=None:return node.val+sumTree(node.left)+sumTree(node.right)
    return 0

myTree = AVL_Tree() 
root = None
k,data = input("Enter Input : ").split('/')
k=int(k)
data = [int(i)for i in data.split()]
if int(k/2)+1!=len(data) or int(k/2)==k/2 or k<3:
    print("Incorrect Input")
    exit(0)
for e in range(k):
    root = myTree.insert(root, 0)
fillData(root,data,k)
cutting(root)
print(sumTree(root))
class Node:
    def __init__(self,data,fre,left=None,right=None):
        self.data = data
        self.fre = fre
        self.left = left
        self.right = right 

def appendNode(l,a,f):
    for i in range(len(l)):
        if l[i].fre <= f:
            return l[:i]+[Node(a,f)]+l[i:]
    return l+[Node(a,f)]

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.data)
        printTree(node.left, level + 1)
        
def buildDic(node,s=""):
    if node:
        global d
        if not node.left:d[node.data] = s
        buildDic(node.right,s+"1")
        buildDic(node.left,s+"0")

d={}
s=input("Enter Input : ")
for i in s:d[i] = d[i]+1 if i in d else 1
nl=[]
for i in d:nl=appendNode(nl,i,d[i])
while len(nl)>1:
    le = nl.pop()
    ri = nl.pop()
    n=Node("*",le.fre+ri.fre,le,ri)
    i=0
    while True:
        if nl==[] or i==len(nl) or nl[i].fre <= n.fre:
            nl=nl[:i]+[n]+nl[i:]
            break
        i+=1
root=nl.pop()
d={}
buildDic(root)
print(d)
printTree(root)
print("Encoded!  : ",end="")
for i in s:print(d[i],end="")

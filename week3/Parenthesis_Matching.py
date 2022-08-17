class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]
    
    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        tmp=self.items[-1]
        self.items.remove(tmp)
        return tmp

s=Stack()
o=["(","{","["]
c=[")","}","]"]
a=input("Enter expresion : ")
print(a,end="")
for i in a:
    if i in o:
        s.push(i)
    elif i in c:
        if s.size()==0:
            print(" close paren excess")
            exit()
        elif o.index(s.top())!=c.index(i):
            print(" Unmatch open-close")
            exit()
        else:
            s.pop()
if s.size()!=0:
    print(" open paren excess   "+str(s.size())+" : ",end="")
    t=""
    while not s.isEmpty():
        t+=s.top()
        s.pop()
    print(t[::-1])

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1] if self.size>0 else -1

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()

s=Stack()
t=Stack()
for i in input("Enter Input : ").split(","):
    if i[0]=='A':
        s.push(int(i[2:]))
        print("Add = "+i[2:])
    elif i[0]=='P':
        if s.isEmpty():
            print(-1)
        else:
            print("Pop = "+str(s.pop()))
    elif i[0]=='D':
        if s.isEmpty():
            print(-1)
        else:
            while not s.isEmpty():
                a=s.pop()
                if a==int(i[2:]):
                    print("Delete = "+str(a))
                else:
                    t.push(a)
            while not t.isEmpty():s.push(t.pop())
    elif i[0]=='L':
        if s.isEmpty():
            print(-1)
        else:
            while not s.isEmpty():
                a=s.pop()
                if a<int(i[3:]):
                    print("Delete =",str(a),"Because",str(a),"is less than",i[3:])
                else:
                    t.push(a)
            while not t.isEmpty():s.push(t.pop())
    else:
        if s.isEmpty():
            print(-1)
        else:
            while not s.isEmpty():
                a=s.pop()
                if a>int(i[3:]):
                    print("Delete =",str(a),"Because",str(a),"is more than",i[3:])
                else:
                    t.push(a)
            while not t.isEmpty():s.push(t.pop())
l=[]
while not s.isEmpty():l.append(s.pop())
print("Value in Stack = "+str(l[::-1]))

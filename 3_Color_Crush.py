class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s
    
    def append(self,data):
        p = Node(data)
        if self.isEmpty():
            self.head = p
        else:
            t=self.head
            while t.next!=None:
                t=t.next
            t.next = p

a=LinkedList()
for i in input("Enter Input : ").split():a.append(i)
t = a.head
combo=0
i=0
while a.size()>2 and t.next.next!=None:
    if i==0 and t.data==t.next.data and t.data == t.next.next.data:
        if a.size()==3:
            a.head = None
            t=a.head
            combo+=1
        else:
            a.head = t.next.next.next
            t = a.head
            combo+=1
        
    elif t.next.data == t.next.next.data and t.next.data == t.next.next.next.data:
        t.next = t.next.next.next.next
        combo+=1
        i=0
        t = a.head
    else:
        t=t.next
        i+=1
print(a.size())
if a.isEmpty():print("Empty")
else:print(a.__str__()[::-1])
if combo>1:print("Combo : "+str(combo)+" ! ! !")
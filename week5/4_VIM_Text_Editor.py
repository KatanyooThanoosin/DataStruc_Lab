class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        p = Node(item)
        if self.isEmpty():
            self.head = p
            self.tail = p
        else:
            p.previous = self.tail
            self.tail.next = p
            self.tail = p
            
    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s

    def insert(self, pos, item):
        p=Node(item)
        n=self.size()
        if self.isEmpty():
            self.head = p
            self.tail = p
        elif pos==0 or -1*pos>n:
            self.head.previous = p
            p.next = self.head
            self.head = p
        elif pos>n-1:
            self.tail.next = p
            p.previous = self.tail
            self.tail = p
        elif pos>0:
            t=self.head
            i = 0
            while i<pos-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next.previous = p
            t.next = p
            p.previous = t
        else:
            t=self.tail
            i = 1
            while i<-1*pos:
                i+=1
                t=t.previous
            p.previous = t.previous
            t.previous.next = p
            t.previous = p
            p.next = t

    def pop(self, pos):
        n=self.size()
        i=0
        t=self.head
        while i<pos and pos<n:
                t=t.next
                i+=1
        if n==1:
            self.head=None
            self.previous=None
        elif i==0:
            self.head = t.next
            self.head.previous = None
        elif i==n-1:
            self.tail = t.previous
            self.tail.next = None
        else:
            t.next.previous = t.previous
            t.previous.next = t.next
        
a=LinkedList()
a.append("|")
curIn = 0
for i in input("Enter Input : ").split(","):
    if i[0]=="I":
        a.insert(curIn,i[2:])
        curIn+=1
    elif i[0]=="L":
        if curIn!=0:
            a.pop(curIn)
            curIn-=1
            a.insert(curIn,"|")
    elif i[0]=="R":
        if curIn!=a.size()-1:
            a.pop(curIn)
            curIn+=1
            a.insert(curIn,"|")
    elif i[0]=="B":
        if curIn!=0:
            curIn-=1
            a.pop(curIn)
    else:
        if curIn!=a.size()-1:
            a.pop(curIn+1)
print(a.__str__())
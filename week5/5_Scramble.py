class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def __str__(self):
        s=""
        t=self.head
        while t!=None:
            s+=str(t.data)
            t=t.next
            if t!=None:s+="->"
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
    
    def insert(self, index, data):
        p=Node(data)
        if self.isEmpty():
            self.head = p
        elif index==0:
            p.next = self.head
            self.head = p
        else:
            t=self.head
            i = 0
            while i<index-1:
                i+=1
                t=t.next
            p.next = t.next
            t.next = p
            
    def pop(self, pos):
        n=SIZE(self)
        i=0
        t=self.head
        while i<pos-1 and pos < n:
            t=t.next
            i+=1
        if n==1:
            self.head=None
        elif pos==0:
            self.head = t.next
        else:
            t.next=t.next.next
        

class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def front(self):
        return self.items[0] if self.size()>0 else -1
    
    def enqueue(self,tmp):
        self.items.append(tmp)
    
    def dequeue(self):
        return self.items.pop(0)

def createLL(LL):
    a=LinkedList()
    for i in LL:a.append(i)
    return a

def printLL(h):
    if h.isEmpty():
        return "Empty"
    cur, s = h.head, str(h.head.data) + " "
    while cur.next != None:
        s += str(cur.next.data) + " "
        cur = cur.next
    return s

def SIZE(h):
    s=0
    t=h.head
    while t!=None:
        s+=1
        t=t.next
    return s

def scarmble(h, b, r, s):
    
    #BottomUp
    for i in range(int(b*s/100)):
        a=h.head.data
        h.pop(0)
        h.append(a)
    print("BottomUp %.3f"%b,"% : "+printLL(h))
    
    #Riffle
    q=Queue()
    a=h.head
    i=0
    while i<int(r*s/100)-1:
        i+=1
        a=a.next
    while a.next != None:
        q.enqueue(a.next.data)
        h.pop(i+1)
    i=1
    while not q.isEmpty() and i<SIZE(h):
        h.insert(i,q.dequeue())
        i+=2
    while not q.isEmpty():h.append(q.dequeue())
    print("Riffle %.3f"%r,"% : "+printLL(h))
    
    #Deriffle
    new = Queue()
    while q.size()<s-int(r*s/100) and new.size()<int(r*s/100):
        new.enqueue(h.head.data)
        h.pop(0)
        q.enqueue(h.head.data)
        h.pop(0)
    if q.size()<s-int(r*s/100):
        while not h.isEmpty():
            q.enqueue(h.head.data)
            h.pop(0)
    else:
        while not h.isEmpty():
            new.enqueue(h.head.data)
            h.pop(0)
    while not new.isEmpty():h.append(new.dequeue())
    while not q.isEmpty():h.append(q.dequeue())
    print("Deriffle %.3f"%r,"% : "+printLL(h))
    
    #Debottomup
    for i in range(s-int(b*s/100)):
        a=h.head.data
        h.pop(0)
        h.append(a)
    print("Debottomup %.3f"%b,"% : "+printLL(h)) 

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        scarmble(h, float(k[1][2:]), float(k[0][2:]),SIZE(h))
    print('-' * 50)
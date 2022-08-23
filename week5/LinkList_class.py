class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

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
    
    def size(self):
        s=0
        t=self.head
        while t!=None:
            s+=1
            t=t.next
        return s
    
    def isEmpty(self):
        return self.head == None
    
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

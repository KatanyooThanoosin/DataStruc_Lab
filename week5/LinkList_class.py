class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        t = self.head
        s=""
        while t != None:
            s+=str(t.data)
            if t.next != None:s+=" -> "
            t = t.next
        return s
    
    def isEmpty(self):
        return self.head==None
    
    def size(self):
        sum = 0
        t = self.head
        while t!=None:
            sum = sum+1
            t=t.next
        return sum
    
    def append(self,i):
        a = Node(i)
        if self.isEmpty():
            self.head = a
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = a
    
    def insert(self, index, data):
        a = Node(data)
        if self.isEmpty():
            self.head = a
        elif index ==0:
            a.next = self.head
            self.head = a
        else:
            t = self.head
            count = 0
            while count < index-1:
                t = t.next
                count+=1
            a.next = t.next
            t.next = a

    def pop(self,index):
        if index == 0:
            a = self.head.data
            self.head = self.head.next
            return a
        else:
            t = self.head
            i = 0
            while i<index-1:
                t = t.next
                i = i+1
            a = t.next.data
            t.next = t.next.next
            return a

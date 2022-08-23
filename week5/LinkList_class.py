class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        l=[]
        t=self.head
        while t!=None:
            l.append(t.data)
            t=t.next
        return l
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

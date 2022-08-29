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
    
q=Queue()
w,h = input("Enter code,hint : ").split(",")
s=ord(h)-ord(w[0])
for i in w:
    q.enqueue(chr(ord(i)+s))
    print(q.items)
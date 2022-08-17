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
    
a=input("Enter people and time : ").split()
n=int(a[1])
q1=Queue()
q2=Queue()
c=0
a=[i for i in a[0]]
for i in range(n):
    if i>0 and i%3==0 and not q1.isEmpty():
        q1.dequeue()
    if c>0 and c%2==0 and not q2.isEmpty():
        q2.dequeue()
    if len(a)>0:
        if q1.size()<5:
            q1.enqueue(a[0])
        else:
            q2.enqueue(a[0])
            if q2.size()==1:c=0
        a=a[1:]
    c+=1
    print(str(i+1)+" "+str(a)+" "+str(q1.items)+" "+str(q2.items))
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
        return self.items.pop(0) if self.size()>0 else -1

q=Queue()
tmp=Queue()
a=input("Enter Input : ").split("/")
b=a[1].split(",")
a=a[0].split(",")
id=[i.split()[1]for i in a]
for i in b:
    if i[0]=="D":
        if q.isEmpty():
            print("Empty")
        else:
            k=q.dequeue()
            a.append(k)
            id.append(k[2:])
            print(k[2:])
    elif i[2:] in id:
        dat=a[id.index(i[2:])]
        while not q.isEmpty() and q.front()[0]!=dat[0]:
            tmp.enqueue(q.dequeue())
        if q.isEmpty():tmp.enqueue(dat)
        else:
            while not q.isEmpty() and q.front()[0]==dat[0]:tmp.enqueue(q.dequeue())
            tmp.enqueue(dat)
            while not q.isEmpty():tmp.enqueue(q.dequeue())
        while not tmp.isEmpty():q.enqueue(tmp.dequeue())
        a.remove(dat)
        id.remove(i[2:])
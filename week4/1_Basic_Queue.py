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

a=input("Enter Input : ").split(",")
q=Queue()
for i in a:
    if i[0]=='E':
        print("Add "+i[2:]+" index is "+str(q.size()))
        q.enqueue(i[2:])
    else:
        x=q.dequeue()
        if x==-1:
            print(x)
        else:
            print("Pop "+x+" size in queue is "+str(q.size()))
if q.isEmpty():
    print("Empty")
else:
    print("Number in Queue is :  ",end="")
    print(q.items)
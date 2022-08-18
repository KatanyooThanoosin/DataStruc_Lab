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
    
n,m=input("Enter Input (Normal, Mirror) : ").split()
mirq=Queue()
mirExCount=0
norExCount=0
fIn=0
i=0
n=[i for i in n]
m=[i for i in m[::-1]]
while i<len(m)-2:
    if m[i]==m[i+1] and m[i]==m[i+2]:
        mirq.enqueue(m[i])
        for j in range(3):m.pop(i)
        i=0
        mirExCount+=1
    else:i+=1
i=0
while i<len(n)-2:
    if n[i]==n[i+1] and n[i]==n[i+2]:
        if mirq.isEmpty():
            for j in range(3):n.pop(i)
            norExCount+=1
        else:
            tmp=mirq.dequeue()
            if tmp!=n[i]:
                n="".join(n)
                n=[i for i in n[:i+2]+tmp+n[i+2:]]
            else:
                for j in range(2):n.pop(i)
                fIn+=1
        i=0
    else:i+=1
print("NORMAL :\n"+str(len(n)))
if len(n)==0:
    print("Empty")
else:
    print("".join(n)[::-1])
print(str(norExCount)+" Explosive(s) ! ! ! (NORMAL)")
if fIn>0:
    print("Failed Interrupted "+str(fIn)+" Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM\n"+str(len(m)))
if len(m)==0:
    print("ytpmE")
else:
    print("".join(m)[::-1])
print("(RORRIM) ! ! ! (s)evisolpxE "+str(mirExCount))
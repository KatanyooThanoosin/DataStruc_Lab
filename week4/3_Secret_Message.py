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
    
a=input("Enter String and Code : ").split(",")
alp=Queue()
num=Queue()
for i in a[0]:
    if ord(i)>=ord('A') and ord(i)<=ord('Z'):alp.enqueue(i)
    elif ord(i)>=ord('a') and ord(i)<=ord('z'):alp.enqueue(i)
for i in a[1]:num.enqueue(int(i))
en=[]
de=[]
while not alp.isEmpty():
    tmp=alp.dequeue()
    a=num.dequeue()
    num.enqueue(a)
    if tmp.isupper():
        en.append(chr(((ord(tmp)+a-ord('A'))%26)+ord('A')))
    else:
        en.append(chr(((ord(tmp)+a-ord('a'))%26)+ord('a')))
    de.append(tmp)
print("Encode message is :  "+str(en))
print("Decode message is :  "+str(de))
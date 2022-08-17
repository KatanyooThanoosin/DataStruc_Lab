class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1] if self.size()>0 else -1

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()
    
def dec2bin(decnum):
    s = Stack()
    while decnum>0:
        s.push(decnum%2)
        decnum=int(decnum/2)
    t=""
    while not s.isEmpty():
        t+=str(s.pop())
    return t
        
print(" ***Decimal to Binary use Stack***")
token = input("Enter decimal number : ")
print("Binary number : ",end='')
print(dec2bin(int(token)))
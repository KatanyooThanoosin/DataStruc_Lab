class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()

def postFixeval(st):
    s = Stack()
    for i in st:
        if i=="+":s.push(s.pop()+s.pop())
        elif i=="-":s.push(-1*s.pop()+s.pop())
        elif i=="*":s.push(s.pop()*s.pop())
        elif i=="/":
            a=s.pop()
            b=s.pop()
            s.push(b/a)
        else:
            s.push(float(i))
    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))
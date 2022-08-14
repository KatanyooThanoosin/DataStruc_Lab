class Stack:
    def __init__(self):
        self.stack = []
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        return self.stack[-1]
    
    def push(self,tmp):
        self.stack.append(tmp)
    
    def pop(self):
        tmp=self.stack[-1]
        self.stack.remove(self.stack[-1])
        return tmp

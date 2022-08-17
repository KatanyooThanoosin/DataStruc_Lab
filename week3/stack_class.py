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
        tmp=self.items[-1]
        self.items.remove(tmp)
        return tmp

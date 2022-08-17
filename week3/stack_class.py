class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def push(self,tmp):
        self.items.append(tmp)
    
    def pop(self):
        return self.items.pop()

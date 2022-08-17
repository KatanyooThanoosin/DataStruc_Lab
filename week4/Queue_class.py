class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0] if self.size()>0 else -1
    
    def enqueue(self,tmp):
        self.queue.append(tmp)
    
    def dequeue(self):
        return self.queue.pop(0) if self.size()>0 else -1

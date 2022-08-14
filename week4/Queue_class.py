class Queue:
    def __init__(self):
        self.queue = []
        
    def isEmpty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        return self.queue[0]
    
    def enqueue(self,tmp):
        self.queue.append(tmp)
    
    def dequeue(self):
        self.queue.remove(self.queue[0])

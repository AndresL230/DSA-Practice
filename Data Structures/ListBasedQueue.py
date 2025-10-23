class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, val):
        self.queue = [val] + self.queue
    
    def dequeu(self):
        self.queue.pop(-1)

    def front(self):
        return self.queue[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0 
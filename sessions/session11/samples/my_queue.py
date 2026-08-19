class Queue:
    def __init__(self):
        self.storage = []
        
    def enqueue(self, data):
        self.storage.insert(0, data)

    def dequeue(self):
        return self.storage.pop()

    @property
    def head(self):
        return self.storage[-1]
    
    def __len__(self):
        return len(self.storage)
    
    def is_empty(self):
        return False if self.storage else True
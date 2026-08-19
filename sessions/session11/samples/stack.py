class Stack:
    def __init__(self):
        self.storage = []

    def push(self, data):
        self.storage.append(data)

    def pop(self):
        return self.storage.pop()
    @property
    def top(self):
        return self.storage[-1]
    
    def __len__(self):
        return len(self.storage)
    
    def is_empty(self):
        # len(self.storage) > 0
        return False if self.storage else True
        if self.storage:
            return False
        else:
            return True
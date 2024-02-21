class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items


    @property  
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        if len(items) <= self.limit:
            self._items = items
        else:
            raise AttributeError("Length of items cannot be greater than the limit.")

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)

    def pop(self):
        if(len(self.items) > 0):
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        i = 1
        for item in self.items:
            if item != target:
                i += 1
            else:
                return len(self.items) - i
        return -1

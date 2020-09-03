# from collections import deque

class RingBuffer:
    def  __init__(self, size):
        self.size = size
        self.storage = []
        self.age = 0

    def push(self, value):
        if len(self.storage) < self.size:
            self.storage.append(value)
        else:
            self.storage[self.age] = value
            if self.age < self.size - 1:
                self.age += 1
            else:
                self.age = 0

        


ring = RingBuffer(3)

ring.push('a')
ring.push('b')
ring.push('c')
print(ring.storage)

ring.push('d')
print(ring.storage)

ring.push('e')
print(ring.storage)
ring.push('f')
print(ring.storage)

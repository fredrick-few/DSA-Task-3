# Illustration of implementation of circular queue using Python
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, item):
        if self.is_full():
            print("Queue Overflow: Cannot insert", item)
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow: Queue is empty")
            return None
        removed = self.queue[self.front]
        if self.front == self.rear:
            # Queue becomes empty after removing the last element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        elements = []
        i = self.front
        while True:
            elements.append(self.queue[i])
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print("Circular Queue:", elements)

# Example Usage
cq = CircularQueue(4)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.dequeue()       # Frees index 0
cq.enqueue(50)     # Wraps around to index 0
cq.display()       # Output: Circular Queue: [20, 30, 40, 50]
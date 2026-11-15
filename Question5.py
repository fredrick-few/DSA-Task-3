# A program to perform enqueuer and dequeuer in a queue
class LinearQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.max_size - 1

    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, item):
        if self.is_full():
            print("Overflow: Queue is full.")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = item
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Underflow: Queue is empty.")
            return None
        item = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = -1
            self.rear = -1
        print(f"Dequeued: {item}")
        return item

    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Current Queue:", self.queue[self.front : self.rear + 1])

# Demonstration
q = LinearQueue(5)
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def display(self):
        print(self.queue)


queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:")
queue.display()

print("\nQueuedan elementni olish:", queue.dequeue())
print("Queueda oldingi element:", queue.front())
print("Queue:")
queue.display()

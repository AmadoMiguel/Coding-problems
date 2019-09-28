# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure
# with the following methods: enqueue, which inserts an element into the queue, and dequeue, which removes it.


class queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) > 0:
            # Remove the first inserted element (FIFO)
            print("Removing first element in the queue...")
            self.queue.pop(0)
    def showQueue(self):
        print(self.queue)


# Create a queue
myQueue = queue()
# Insert some elements to it
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(5)
myQueue.enqueue(6)
myQueue.enqueue('o')
# View
myQueue.showQueue()
# Delete the first element that was inserted to the queue
myQueue.dequeue()
# View and verify removal
myQueue.showQueue()


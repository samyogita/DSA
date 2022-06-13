class Queue:
    def __init__(self):
        self.items = []
    
    def __str__(self):
        values = [str(x) for x in self.items]
        return '\n'.join(values)
    
    # isEmpty 
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
    
    # Enqueue 
    def enqueue(self, value):
            self.items.append(value)
            return "The element has is inserted at the end of the queue"
    
    # Dequeue
    def dequeue(self):
        if self.isEmpty():
            return "The is not any element in the queue"
        else:
            return self.items.pop(0)
    
    # Peek 
    def peek(self):
        if self.isEmpty():
            return "The is not any element in the queue"
        else:
            return self.items[0]

    # delete
    def delete(self):
        self.items = None

    

customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())
customQueue.delete()




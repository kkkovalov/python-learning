class QueueObject:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, queues=[]):
        self.head = None
        self.tail = None
        if queues is not None:
            c_queue = QueueObject(data=queues.pop(0))
            self.head = c_queue
            self.tail = c_queue
            for item in queues:
                c_queue.next = QueueObject(data=item)
                c_queue = c_queue.next
            self.tail = c_queue
        
        
    
    def __repr__(self):
        first_in_queue = self.head
        queue = []
        while first_in_queue is not None:
            queue.append(str(first_in_queue.data))
            first_in_queue = first_in_queue.next
        queue.append('None')
        return '->'.join(queue)
    
    def __iter__(self):
        first_in_queue = self.head
        while first_in_queue is not None:
            yield first_in_queue.data
            first_in_queue = first_in_queue.next
    
    def enqueue(self, data):
        new_item = QueueObject(data=data)
        self.tail.next = new_item
        return None
    
    def dequeue(self):
        removed_item = self.head.data
        self.head = self.head.next
        return removed_item    
        
    def front(self):
        return self.head.data
    
    def last(self):
        return self.tail.data
        
            
    


qqueue = Queue([1,4,9,23,43,8,3])

print(qqueue)

print(qqueue.front(), qqueue.last())

qqueue.enqueue(431)
qqueue.dequeue()
qqueue.dequeue()

print(qqueue)
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
            
    def 
            
    


qqueue = Queue([1,4,9,23,43,8,3])

for item in qqueue:
    print(item)
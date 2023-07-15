INITIAL_CAPACITY = 50

class HashTable:
    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity
    
    def c_hash(self, key):
        return hash(key)
        # hashsum = 0
        # for idx, c in enumerate(key):
        #     hashsum+=(idx + len(key)) ** ord(c)
        #     hashsum = hashsum % self.capacity
        # return hashsum
    
    def insert(self, key, value):
        self.size+=1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)
        
    def __repr__(self):
        node = self.buckets[0]
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append('None')
        return "->".join(nodes)
    
    
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return "->".join(str(self.key), str(self.value))
    
    
    
hhash = HashTable()

hhash.insert('name', 'Vlad')
hhash.insert('age', 13)
hhash.insert('city', 'Kelowna')
hhash.insert('country', 'Canada')

print(hhash)

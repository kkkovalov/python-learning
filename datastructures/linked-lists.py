# Linked lists
# [] - insert, first, end, between
# [] - traverse
# [] - delete
# [] - 

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __repr__(self):
        return self.data
        
class LinkedList:
    
    def __init__(self, nodes = []):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(data=item)
                node = node.next
                
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return "->".join(nodes)
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, data):
        node = Node(data=data)
        node.next = self.head
        self.head = node
    
    def add_last(self, data):
        node = Node(data=data)
        c_node = self.head
        while c_node.next is not None:
            c_node = c_node.next
        c_node.next = node
        
    def insert(self, position, data):
        node = Node(data=data)
        if self.head is None:
            self.head = node
            return None
        c_node = self.head
        for i in range(0,position-2):
            c_node = c_node.next
        node.next = c_node.next
        c_node.next = node
            
    def remove(self, target_node):
        if self.head is None:
            raise Exception("List is empty")
        
        if self.head.data == target_node:
            self.head = self.head.next
        
        previous_node = self.head
        for node in self:
            if node.data == target_node:
                previous_node.next = node.next
                return None
            previous_node = node
        
        raise Exception("Node with data '%s' not found" % target_node)
        
        
        
llist = LinkedList(['a','b','c','d','e', 'g'])

print(llist)

llist.add_first('h')

llist.add_last('t')
llist.insert(3,'r')

print(llist)

    


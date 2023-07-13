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
        
        
        
        
        
llist = LinkedList([1,4,51,52,61,23,40])

print(llist)


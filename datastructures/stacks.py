class StackObject:
    
    """
    Testing the stack object/node
    
    >>> node = StackObject(1)
    >>> print(node.next)
    None
    
    """
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class Stack:
    def __init__(self, init_stack = []):
        self.head = None
        
        if init_stack is not None:
            stack_item = StackObject(data=init_stack.pop(0))
            self.head = stack_item
            for item in init_stack:
                new_item = StackObject(data=item)
                new_item.next = self.head
                self.head = new_item
        return None
    
    def __repr__(self):
        if self.head is not None:
            stack = self.head
            stacks = []
            while stack is not None:
                stacks.append(str(stack.data))
                stack = stack.next
            stacks.append('None')
            return "->".join(stacks)
    
    def pop(self):
        removed_item = self.head.data
        self.head = self.head.next
        return removed_item

    def push(self, data):
        new_stack_item = StackObject(data=data) 
        if self.head is None:
            self.head = new_stack_item
            return None
        previous_head = self.head
        self.head = new_stack_item
        new_stack_item.next = previous_head
    
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
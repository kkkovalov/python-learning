class StackObject:
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
    

new_stack = Stack([4,6,1,8,2,0])

print(new_stack)
class Stack:
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, new_item):
        """Adds item to end"""
        return self.items.append(new_item)

    def pop(self):
        """Removes items from end"""
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

def reversed_list(orig_list):
    """
    Write a function that uses a stack
    to return a reversed copy of a list.
    """
    my_stack = Stack(orig_list)
    result = []

    while not my_stack.is_empty():
        result.append(my_stack.pop())
    return result


class Queue(Stack):
    def __init__(self, items=[]):
        self.items = items

    def enqueue(self, item):
        """Adds item to beg"""
        return self.items.insert(0, item)

    def dequeue(self):
        """Removes item from end"""
        return super().pop()

    def is_empty(self):
        return super().is_empty()

    def size(self):
        return super().size()

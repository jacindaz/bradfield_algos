class Stack:
    """ LIFO: last in first out """
    def __init__(self, items=[]):
        self.items = items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, new_item):
        """ Adds item to end """
        return self.items.append(new_item)

    def pop(self):
        """ Removes items from end """
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
    """ FIFO: first in first out """
    def __init__(self, stack):
        self.stack = stack

    def enqueue(self, new_item):
        """ Adds item to beg """
        reversed_stack = Stack(reversed_list(self.stack.items))
        new_stack = Stack([])
        new_stack.push(new_item)

        while not reversed_stack.is_empty():
            to_add = reversed_stack.pop()
            new_stack.push(to_add)

        self.stack = new_stack
        return new_stack


    def dequeue(self):
        """ Removes item from end """
        return self.stack.pop()

    def is_empty(self):
        return self.stack.is_empty()

    def size(self):
        return self.stack.size()

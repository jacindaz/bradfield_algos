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


def reversed_list(my_stack):
    """
    Write a function that uses a stack
    to return a reversed copy of a list.
    """
    result = []
    while not my_stack.is_empty():
        result.append(my_stack.pop())
    return result


class Queue(Stack):
    """ FIFO: first in first out """
    def __init__(self, stack):
        self.stack = stack

    def enqueue(self, new_item):
        """ Adds item to end """
        return self.stack.push(new_item)

    def dequeue(self):
        """ Removes item from front """
        reversed_stack = Stack(reversed_list(self.stack))
        removed_item = reversed_stack.pop()

        self.stack = Stack(reversed_list(reversed_stack))
        return removed_item

    def is_empty(self):
        return self.stack.is_empty()

    def size(self):
        return self.stack.size()

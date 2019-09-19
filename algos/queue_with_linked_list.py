class Node():
    def __init__(self, value, nex=None, prev=None):
        self.value = value
        self.next = nex
        self.previous = prev

class LinkedList():
    def __init__(self, head=None):
        self.head = head


node1 = Node(1)


class Queue:
    """ FIFO: first in first out """
    def __init__(self, items=None):
        self.linked_list = LinkedList()

        if items:
            current_node = None
            for item in items:
                if self.linked_list.head is None:
                    self.linked_list.head = Node(item)
                    current_node = self.linked_list.head
                else:
                    new_node = Node(item)
                    current_node.next = new_node
                    current_node = new_node

    def enqueue(self, new_value):
        """ Adds item to end """

        if self.linked_list.head is None:
            self.linked_list.head = Node(new_value)

        else:
            current_node = self.linked_list.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(new_value)

    def dequeue(self):
        """ Removes item from front """
        pass

    def is_empty(self):
        pass

    def size(self):
        pass


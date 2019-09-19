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


def balanced_parens(string):
    # if open parens
    # create a stack
    # when close, pop from the stack
    OPEN = "("
    CLOSE = ")"
    paren_items = list(string)
    my_stack = Stack()

    for item in paren_items:
        if item == OPEN:
            my_stack.push(item)
        elif item == CLOSE:
            # if there are items in the stack
            if my_stack.is_empty():
                return False
            my_stack.pop()

    return my_stack.is_empty()


# print(balanced_parens("()((())"))   # false, more open
# print(balanced_parens("()(()))"))    # false, more closed
# print(balanced_parens("()(())"))    # true


def balanced_symbols(string):
    OPEN = ["(", "[", "{"]
    CLOSE = [")", "]", "}"]
    CLOSE_OPEN_MAPPING = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    symbol_items = list(string)
    my_stack = Stack()

    for item in symbol_items:
        print(f"\nitem: {item}, stack: {my_stack.items}")

        if item in OPEN:
            my_stack.push(item)
        elif item in CLOSE:
            print("closed item")
            # stack cannot be empty
            # last item on stack must match mapping
            if my_stack.is_empty():
                return False
            else:
                last_item = my_stack.peek()
                print(f"last_item: {last_item}")
                if last_item != CLOSE_OPEN_MAPPING[item]:
                    return False
                else:
                    print("match, popping\n")
                    my_stack.pop()

    return my_stack.is_empty()

# print(balanced_symbols("([{})]"))    # false
print(balanced_symbols("([({})])"))    # true

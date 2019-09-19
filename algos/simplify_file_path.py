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


# TO DO: can simplify this, how?
def simplify_file_path(file_path):
    file_path_list = file_path.split("/")

    new_path = []
    popped_values = Stack()
    for value in file_path_list:
        if value == "..":
            removed = new_path.pop()
            popped_values.push(removed)
        elif value == ".":
            if previous_value == "..":
                new_path.append(popped_values.pop())
        else:
            new_path.append(value)

        previous_value = value

    return '/'.join(new_path)

# print(simplify_file_path("/usr/elliott/foo/.././bar"))
# print(simplify_file_path("/usr/jz/../foo/bar"))


print(simplify_file_path("/usr/jz/../foo/bar/../blah/hi/./again"))   # /usr/foo/blah/hi/again



# FILL IN

def simplify_file_path2():
    """ do with list only """
    pass


def simplify_file_path3():
    """ do with stack only """
    pass



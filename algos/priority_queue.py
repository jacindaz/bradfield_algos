class MinBinaryHeap:

    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self, new_item):
        new_item_index = self.__len__()
        parent_index = new_item_index // 2
        parent = self.items[parent_index]

        while new_item < parent:
            self.items[new_item_index] = parent
            self.items[parent_index] = new_item

            new_item_index = parent_index
            parent_index = new_item_index // 2
            parent = self.items[parent_index]

    def insert(self, new_item):
        self.items.append(new_item)
        self._percolate_up(new_item)

    def _percolate_down(self, item_to_percolate):
        item_to_percolate_index = 1

        while item_to_percolate_index*2 < self.__len__():
            left_child_index = 2*item_to_percolate_index
            right_child_index = (2*item_to_percolate_index) + 1

            # swap if left child is smaller than item_to_percolate
            if left_child < item_to_percolate:
                self.items[left_child_index] = item_to_percolate
                self.items[item_to_percolate_index] = left_child
                item_to_percolate_index = left_child_index

            # swap if right child is smaller than item_to_percolate
            elif right_child < item_to_percolate:
                self.items[right_child_index] = item_to_percolate
                self.items[item_to_percolate_index] = right_child
                item_to_percolate_index = right_child_index


    def delete_min(self):
        """
        Since in a min binary heap the root is the smallest item,
        you always start by removing the root, then percolate down
        """
        # Start by swapping the root and the last item in the tree
        # then percolate the swapped item down to its proper position
        root = self.items[1]
        last_item = self.items[-1]
        self.items[1] = last_item
        self.items[-1] = root
        self.items.pop()
        self._percolate_down(self.items[1])

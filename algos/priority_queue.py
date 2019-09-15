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
            print(f"\nnew_item_index: {new_item_index}, new_item: {new_item}")
            print(f"parent_index: {parent_index}, parent: {parent}")

            print(f"\nswapping! old self.items: {self.items}")
            self.items[new_item_index] = parent
            self.items[parent_index] = new_item
            print(f"swapped self.items: {self.items}")

            new_item_index = parent_index
            parent_index = new_item_index // 2
            parent = self.items[parent_index]
            print(f"new_item_index reset: {new_item_index}")

    def insert(self, new_item):
        self.items.append(new_item)
        self._percolate_up(new_item)

    def _percolate_down(self, item_to_percolate):
        item_to_percolate_index = 1
        done = False

        while done is False:
            # Stop:
            #   => item_to_percolate at bottom of the tree (no children)
            #      bottom of the tree: means does not have any children
            #   => children of item_to_percolate are both bigger
            if item_to_percolate_index == self.__len__():
                done = True
                print(f"\ndone! final list: {self.items}\n")
                return
            else:
                left_child_index = 2*item_to_percolate_index
                right_child_index = (2*item_to_percolate_index) + 1

                left_child = self.items[left_child_index]
                right_child = self.items[right_child_index]

                print("\n==================================\n")
                print(f"item_to_percolate_index: {item_to_percolate_index}")
                print(f"left_child_index: {left_child_index}, left_child: {left_child}")
                print(f"right_child_index: {right_child_index}, right_child: {right_child}")
                print(f"self.items: {self.items}")

                # swap if left child is smaller than item_to_percolate
                if left_child < item_to_percolate:
                    self.items[left_child_index] = item_to_percolate
                    self.items[item_to_percolate_index] = left_child

                    print(f"\nswapped left!")
                    print(self.items)

                    item_to_percolate_index = left_child_index
                    print(f"updated item_to_percolate_index: {item_to_percolate_index}")

                # swap if right child is smaller than item_to_percolate
                elif right_child < item_to_percolate:
                    self.items[right_child_index] = item_to_percolate
                    self.items[item_to_percolate_index] = right_child

                    print(f"\nswapped right!")
                    print(self.items)

                    item_to_percolate_index = right_child_index
                    print(f"updated item_to_percolate_index: {item_to_percolate_index}")


    def delete_min(self):
        """
        Since in a min binary heap the root is the smallest item,
        you always start by removing the root, then percolate down
        """

        # Start by swapping the root and the last item in the tree
        # then percolate the swapped item down to its proper position
        root = self.items[1]
        last_item = self.items[-1]
        print(f"self.items before swap: {self.items}")

        self.items[1] = last_item
        self.items[-1] = root
        print(f"self.items after swap: {self.items}")

        # pop last item
        self.items.pop()

        self._percolate_down(self.items[1])


bh = MinBinaryHeap([0,5,9,11,14,18,19,21,33,17,27])
# bh.insert(7)
bh.delete_min()  # 5 is the min

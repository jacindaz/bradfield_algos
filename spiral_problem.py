class Spiral():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.current = 1
        self.current_ring = 1
        self.current_height = 0
        self.current_width = 0
        self.result = []

        self.done = False

    def run(self):
        self.build_result()

        if self.result[0][0] is None:
            self.result[0][0] = self.current

        while done is False:
            self.right()
            self.down()
            self.left()
            self.up()
            self.current_ring += 1

    def build_result(self):
        self.result = []

        for he in range(self.height):
            row = []
            for wi in range(self.width):
                row.append(None)
            self.result.append(row)

    def right(self):
        print(f"\nright method")
        while self.current_width < (self.width - self.current_ring):
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

            self.current += 1
            self.current_width += 1
            self.result[self.current_height][self.current_width] = self.current

            if self.current >= (self.height * self.width):
                break

    def down(self):
        print(f"\ndown method")

        while self.current_height < self.height-1:
            self.current += 1
            self.current_height += 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

            # if self.current_ring == 2:
            #     import ipdb; ipdb.set_trace()

            if self.current >= (self.height * self.width):
                # TODO: need to figure out how to break out of loops
                # internet says not good to have 2 while loops
                break

    def left(self):
        print(f"\nleft method")

        # will not work later when going left for inner rings
        while self.current_width > 0:
            self.current += 1
            self.current_width -= 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

            if self.current >= (self.height * self.width):
                break

    def up(self):
        print(f"\nup method")

        while self.current_height > self.current_ring:
            self.current += 1
            self.current_height -= 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

            if self.current >= (self.height * self.width):
                break


spiral = Spiral(3, 4)
spiral.run()
print(spiral.result)

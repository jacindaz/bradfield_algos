class Spiral():
    def __init__(self, height, width):
        self.height = height
        self.width = width

        self.current = 1
        self.current_ring = 1
        self.current_height = 0
        self.current_width = 0
        self.result = []

    def run(self):
        self.build_result()

        if self.result[0][0] is None:
            self.result[0][0] = self.current

        # while self.current <= (self.height * self.width):
        self.right()
        self.down()
        self.left()
        self.up()
            # self.current_ring += 1

    def build_result(self):
        self.result = []

        for he in range(self.height):
            row = []
            for wi in range(self.width):
                row.append(None)
            self.result.append(row)

    def right(self):
        print(f"right method")
        while self.current_width < (self.width - self.current_height -1):
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

            self.current += 1
            self.current_width += 1
            self.result[self.current_height][self.current_width] = self.current

    def down(self):
        print(f"\ndown method")

        while self.current_height < self.height-1:
            self.current += 1
            self.current_height += 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

    def left(self):
        print(f"\nleft method")

        # will not work later when going left for inner rings
        while self.current_width > 0:
            self.current += 1
            self.current_width -= 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")

    def up(self):
        print(f"\nup method")

        while self.current_height > self.current_ring:
            self.current += 1
            self.current_height -= 1
            self.result[self.current_height][self.current_width] = self.current
            print(f"current_height: {self.current_height}, current_width: {self.current_width}")


spiral = Spiral(3, 4)
spiral.run()
print(spiral.result)

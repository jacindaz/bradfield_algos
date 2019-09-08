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

        while self.done is False:
            if self.done is False:
                self.right()
            if self.done is False:
                self.down()
            if self.done is False:
                self.left()
            if self.done is False:
                self.up()
            self.current_ring += 1

    def is_done(self):
        if self.current >= (self.width * self.height):
            self.done = True
        else:
            self.done = False

    def _log_state(self):
        print(f"current_height: {self.current_height}, current_width: {self.current_width}, self.current: {self.current}")

    def build_result(self):
        self.result = []

        for he in range(self.height):
            row = []
            for wi in range(self.width):
                row.append(None)
            self.result.append(row)

    def right(self):
        print(f"\nright method")
        while self.current_width < (self.width-self.current_ring):
            self._log_state()
            self.current += 1
            self.current_width += 1
            self.result[self.current_height][self.current_width] = self.current

        self.is_done()

    def down(self):
        print(f"\ndown method")

        while self.current_height < (self.height-self.current_ring):
            self._log_state()
            self.current += 1
            self.current_height += 1
            self.result[self.current_height][self.current_width] = self.current

        self.is_done()

    def left(self):
        print(f"\nleft method")
        while self.current_width > (self.current_ring-1):
            self._log_state()
            self.current += 1
            self.current_width -= 1
            self.result[self.current_height][self.current_width] = self.current

        self.is_done()

    def up(self):
        print(f"\nup method")
        while self.current_height > self.current_ring:
            self._log_state()
            self.current += 1
            self.current_height -= 1
            self.result[self.current_height][self.current_width] = self.current

        self.is_done()

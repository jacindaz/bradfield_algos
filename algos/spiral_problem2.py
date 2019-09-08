"""
Take two of the spiral problem. Implement:
    => turn() function
    => state: current_direction, height_changes + width_changes
    => is_valid() function
"""


def turn():
    pass


def is_valid():
    # if height and width are valid
    # if current value is not None
    # (we haven't seen this value before)


# Directions:
# right: 0
# down: 1
# left: 2
# up: 3
def run(height, width):
    current_direction = 0
    height_changes = [0, 1, 0, -1]
    width_changes = [1, 0, -1, 0]

    # Compute look-ahead
    # Is valid
    #   => if not valid, turn
    #


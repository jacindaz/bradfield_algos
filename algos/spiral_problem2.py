# Directions:
# RIGHT = 0
# DOWN = 1
# LEFT = 2
# UP = 3
def build_spiral(height, width):
    """
    Simpler solution where we keep track of direction instead,
    and store width/height changes needed per direction.

    Checks if the "next move" in any particular direction is valid,
    if not, turns.

    Manually loops back from "up" direction to "right" direction.
    """
    result = [[None]*width for h in range(height)]

    current_direction = 0
    width_changes = [1, 0, -1, 0]
    height_changes = [0, 1, 0, -1]

    current_width = 0
    current_height = 0
    current_value = 1

    for current_value in range(1, width*height+1):
        result[current_height][current_width] = current_value

        next_width = current_width + width_changes[current_direction]
        next_height = current_height + height_changes[current_direction]

        print(f"\ncurrent_value: {current_value}")
        print(f"next_width: {next_width}, next_height: {next_height}")
        print(f"result: {result}")

        if next_height < height and next_height >= 0 and next_width < width and next_width >= 0 and result[next_height][next_width] is None:
            current_width = next_width
            current_height = next_height
        else:
            print(f"\nturned. old direction: {current_direction}")

            if current_direction == 3:
                current_direction = 0
            else:
                current_direction += 1
            print(f"new direction: {current_direction}. current_value: {current_value}")

            current_width = current_width + width_changes[current_direction]
            current_height = current_height + height_changes[current_direction]
    return result

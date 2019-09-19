# Below is a function called hash that takes a
# string and a table size and returns the hash value
# in the range from 0 to tablesize - 1.


def hash(string, table_size):
    """
    Below is a function called hash that takes a
    string and a table size and returns the hash value
    in the range from 0 to tablesize - 1.
    """
    string_as_ints = [ord(char) for char in string]
    return sum(string_as_ints) % table_size


def hash_with_weighting(string, table_size):
    """
    Same as above but take into account character
    position in the string so that anagrams do not
    have the same hash value.
    """
    string_as_ints = [(ord(char) + index) for index, char in enumerate(list(string))]
    return sum(string_as_ints) % table_size

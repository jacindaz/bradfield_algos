from collections import Counter
import random
import time


def have_duplicates_n_squared(array):
    for index, item in enumerate(array):
        for index2, item2 in enumerate(array[(index+1):]):
            if item == item2:
                return True
    return False


def have_duplicates1(array):
    """ O(n) solution """
    result = Counter(array)
    return len(array) != len(result)


def have_duplicates_set(array):
    """ O(n) solution """
    result = set(array)
    return len(array) != len(result)


def have_duplicates2(array):
    """
    O(n) solution, same as above, but builds
    dictionary manually.
    """
    result = {}
    for char in array:
        if result.get(char):
            return True
        else:
            result[char] = 1
    return False


def have_duplicates3(array):
    """ O(n log n) solution """
    array_sorted = sorted(array)
    previous_item = array_sorted[0]
    for index, item in enumerate(array_sorted):
        # if seen prevoius item
        if index > 0 and previous_item == item:
            return True
    return False


def timing(list_length):
    total = 0
    random_num_list = list(range(list_length))

    start = time.time()
    have_duplicates3(random_num_list)
    end = time.time()

    total += (end-start)

    print(f"num_times ran: {list_length}, total: {total}, avg: {total/list_length}")


# timing(100)
# timing(1000)
# timing(10000)
# timing(100000)
# timing(1000000)
# timing(10000000)

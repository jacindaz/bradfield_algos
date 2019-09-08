from collections import Counter
import random
import time


def have_duplicates1(array):
    """ O(n) solution """
    result = Counter(array)
    return len(array) == len(result)

def have_duplicates2(array):
    result = {}

    for char in array:
        if result.get(char):
            return True
        else:
            result[char] = 1
    return False



def have_duplicates2(array):
    """ O(n log n) solution """
    array_sorted = sorted(array)
    previous_item = array_sorted[0]
    for index, item in enumerate(array_sorted):
        # if seen prevoius item
        if index > 0 and previous_item == item:
            return True

    return False

# print(have_duplicates2([1,2,1]))
# print(have_duplicates2([1,2,3]))


def timing(list_length):
    total = 0
    for _ in range(list_length):
        start = time.time()

        random_num_list = [n for n in range(list_length)]
        # have_duplicates2(random_num_list)
        end = time.time()
        total += (end-start)

    print(f"num_times ran: {list_length}, total: {total}, avg: {total/list_length}")


timing(100)
timing(1000)
timing(10000)
timing(100000)
timing(1000000)
timing(10000000)

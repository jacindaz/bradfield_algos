def calculate_sum(number_to_sum):
    """Linear time solution"""
    sum = 0
    for i in range(1, number_to_sum+1):
        sum += i
    return sum

# print(calculate_sum(3)) # 3+2+1=6
# print(calculate_sum(11))


def calculate_sum_constant_time(number_to_sum):
    """Constant time solution"""
    if number_to_sum % 2 == 0:
        pairs = number_to_sum // 2
        pair_sum = 1 + number_to_sum
        return pairs * pair_sum
    else:
        number_to_sum -= 1
        pairs = number_to_sum // 2
        pair_sum = 1 + number_to_sum
        return (pairs * pair_sum)+(number_to_sum+1)

# print(calculate_sum_more_performant(4)) # 1 + 2 + 3 + 4 = 5+5 = 10
# print(calculate_sum_more_performant(3)) # 6, 1+2+3
# print(calculate_sum_more_performant(11)) #


def calculate_sum_math_formula(n):
    """Constant time solution"""
    return n * (n + 1) // 2

# print(calculate_sum_math_formula(11))
# print(calculate_sum_math_formula(3))

import time
def sum_to_n(n):
    # record start time
    start = time.time()

    # run the function's code
    total = 0
    for i in range(n + 1):
        total += i

    # record end time
    end = time.time()

    return total, end - start

output_template = '{}({}) = {:15d} ({:8.7f} seconds)'
for i in range(1, 10):
    print(output_template.format('sum_to_n', i * 1000000, *sum_to_n(i * 1000000)))

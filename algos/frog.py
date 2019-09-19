def num_paths(end_num):
    # base ??
    if end_num == 1:
        return 1

    if end_num == 2:
        return 2

    # break down problem
    return num_paths(end_num-1) + num_paths(end_num-2)
    # return num_paths(end_num-1)

print(num_paths(4))   # expect: 5
# print(num_paths(6))

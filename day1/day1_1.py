# sort left and right.
# For each number pair:
# - calculate diffence
# Sum the diffences


def split_list_in_two(list_to_split):
    left_list = []
    right_list = []

    for line in list_to_split:
        left_and_right = line.split()
        left_value = left_and_right[0]
        right_value = left_and_right[len(left_and_right) - 1]
        left_list.append(left_value)
        right_list.append(right_value)
    return (left_list,right_list)

filename = 'input'

with open(filename) as f:
    # content is a list of strings, ["1234   5678",
    #                                ...    ...   ] 
    content = f.read().splitlines()

    left_list,right_list = split_list_in_two(content)
   # total_distances = 0
    # line is a string. An element of a list of strings is a string
    
    left_list.sort()
    right_list.sort()
    total_distances = sum([abs(int(x) - int(y)) for x,y in zip(left_list, right_list)])

    print(total_distances)

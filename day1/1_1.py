# sort left and right.
# For each number pair:
# - calculate diffence
# Sum the diffences


filename = 'input'

with open(filename) as f:
    # content is a list of strings, ["1234   5678",
    #                                ...    ...   ] 
    content = f.read().splitlines()

    left_list = []
    right_list = []
   # total_distances = 0
    # line is a string. An element of a list of strings is a string
    for line in content:
        left_and_right = line.split()
        left_number = left_and_right[0]
        right_number = left_and_right[len(left_and_right) - 1]
        left_list.append(left_number)
        right_list.append(right_number)
    
    left_list.sort()
    right_list.sort()
    total_distances = sum([abs(int(x) - int(y)) for x,y in zip(left_list, right_list)])

    print(total_distances)

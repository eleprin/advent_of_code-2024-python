"""For each number in the left list
    - Check occurences in the right list
    - add the number * occurences
    - sum all the values"""

from day1_1 import split_list_in_two
filename = 'input'
with open(filename) as f:
    content = f.read().splitlines()

    left_list,right_list = split_list_in_two(content)
    list_of_scores = []

    for left_number in left_list:
        counter = 0
        for right_number in right_list:
            if left_number == right_number:
                counter += 1
        number_to_add = int(left_number) * counter
        list_of_scores.append(number_to_add)
    print(sum(list_of_scores))

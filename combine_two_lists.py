# There needs to be two lists. From list one, get the odd numbers.
# From list two get the even numbers and make a new list.

def combine_two_lists(list1, list2):
    final_list = []

    for number in list1:
        if number % 2 != 0:
            final_list.append(number)

    for number in list2:
        if number % 2 == 0:
            final_list.append(number)

    return final_list


print(combine_two_lists([10, 20, 41, 53], [45, 67, 72, 80]))

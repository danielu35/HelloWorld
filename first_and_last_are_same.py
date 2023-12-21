# Write a function to check the first and last number of a list to see if they are the same.
# If they are, return True. If they are not, return False.

def check_first_and_last(*numbers):
    print(numbers[0], numbers[-1])
    if numbers[0] == numbers[-1]:
        return True
    else:
        return False


print(check_first_and_last(1, 2, 3, 4, 5, 1))
print(check_first_and_last(1, 2, 3, 4, 5))

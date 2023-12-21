# Given two integer numbers, return their product only if the product
# is equal to or lower that 1,000. Otherwise, return their sum. 

def multiplication_or_sum(num1, num2):
    multiplied_total = num1 * num2
    if multiplied_total <= 1000:
        return multiplied_total
    else:
        return num1 + num2


num1 = input("Please enter a number: ")
num2 = input("Please enter another number: ")

result = multiplication_or_sum(int(num1), int(num2))

print(f"The result is {result}")
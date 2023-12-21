# Write a program to iterate the first 10 numbers, and in each iteration,
# print the sum of the current and previous number.

print("Printing current and previous number sum in a range(10)")

for number in range(10):
    current_number = number
    previous_number = number if number == 0 else number - 1
    sum_of_numbers = current_number + previous_number
    print(f"Current Number {current_number} Previous Number {
          previous_number} Sum: {sum_of_numbers}")

# Write a program to extract each digit from a number in reverse order
# and add a space inbetween each digit.
# Example: 1234
# Expected outcome: 4 3 2 1

number = input("Enter a number: ")
print(" ".join(number[::-1]))
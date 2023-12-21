# Make sure the number is a palindrone number and return yes or no
# Example: 121 is True. This number is the same backwards
# Example: 123 is False. This number is not the same backwards

def is_palindrone_number(number):
    print(f"Original number is {number}")
    reverse = number[::-1]
    if number == reverse:
        print("Yes. GIven number is a palindrone number")
    else:
        print("No. Given number is not a palindrone number")


is_palindrone_number(
    input("Enter a number to know if its a palindrone number: "))

# Divisable by 3: Fizz
# Divisable by 5: Buzz
# Divisable by both 3 and 5: FizzBuzz
# Any other number, return the number that was inputed

def FizzBuzz(input):
    if (input % 3 == 0) & (input % 5 == 0):
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else: 
        return input
    

input = input("Enter a number: ")
print(FizzBuzz(int(input)))
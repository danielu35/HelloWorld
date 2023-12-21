# Iterate through the given list of numbers and print only those numbers that are divisable by 5

def divisable_by_5(list):
    print(f"Given list is: {list}")
    print("Divisible by 5")
    for number in list:
        if number % 5 == 0:
            print(number)

divisable_by_5([10, 20, 33, 46, 55])
# Write a program the removes characters from a string starting from 0 to n
# and return a new string
# Example: 
    # remove_char("pynative", 2) should retirn or print "native" and remove "py"

def split_string(string, index):
    if index < len(string):
        result_string = string[index:]
        return result_string
    else:
        print("Enter a nimber that is smaller then the amount of characters in the string.")


string = input("Please enter a word: ")
index = input("Enter the index where you want to split the string: ")
print(split_string(string, int(index)))
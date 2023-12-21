# Count the number of times the substring inputed appers in the string given.

def count_substring(string, substring):
    count = string.lower().count(substring.lower())
    print(f"The word {substring} appeared {count} time in the string: '{string}'")


string = input("Please enter a sentance or a phrace: ")
substring = input("Enter a word you wish to know how many times it appears: ")
count_substring(string, substring)

# Write a program to accept a strign from the user and display
# characters that are prosent at an even index number

string = input("Please enter a word: ")
print(f"The word is {string}")
print("We will only print the even indexes in the word")
index = 0
for letter in string:
    if index % 2 == 0:
        print(letter, index)
        index += 1
    else: 
        index += 1
#!/Users/frank.baileyaxonius.com/.pyenv/shims/python

# importing argv from sys
from sys import argv

# declaring variables for arguments provided
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't what, hit CTRL-C (^C).")
print("If you want that, hit RETURN.")

input("?")

# opening the file using the open function
print("Opening the file...")
target = open(filename, 'w')

# erasing the file using the truncate function
# print("Truncating the file. Goodbye!")
# target.truncate()


# receiving strings to put into the file
print("Now I'm going to ask  you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# writing the strings to the file
print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

# closing the file using the close function
print("And finally, we close it.")
target.close()


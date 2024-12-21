# Ask user to enter sentence with input,
# variable = str_manip
str_manip = input("Enter a sentence:")

#  Calculate and display the length of str_manip
print(len(str_manip))

# Find the last letter in str_manip sentence. 

print(str_manip[-1:])

# Replace every occurrence of this 
# letter in str_manip with ‘@’.

rep_char = str_manip[-1:]
new_char = '@'
str_manip_rep = str_manip.replace(rep_char, new_char)
print(str_manip_rep)

#  Print the last three characters in str_manip backwards.

print(str_manip[-1:-4:-1])

# Create a five-letter word that is made up of the 
# first three characters and the last 
# two characters in str_manip

five_word = (str_manip[0:3]) + (str_manip[-2:])
print(five_word)
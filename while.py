

#  Write a program that continually asks the user to enter a number.

# The programme brief requires that a value of entered numbers is needed
# this means including code to add the numbers and the nuo. of iterations
total = 0
count = 1

# Input the number and turn to an integer
num = int(input("Enter a number: "))
print(num)

# three conditions are needed in the while Loop
# 1) -1 must break the loop, 0 is to be discounted, 
# and number must be 1 or more
while True:
    num = int(input("Enter a number: "))
    if num == -1:
        break
    if num == 0:
        continue
    if num > 0:
        print(num)
# include the counters
        total += num
        count += 1

# explain the results to the user
print(f"Total entries: {count}")
print(f"Total sum of numbers is {total}")

average = total // count
print(f"The average of the numbers you input is {average}")
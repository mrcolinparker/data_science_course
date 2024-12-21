# ● Ask the user to enter three different integers.


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

# Then print out:
# The sum of all the numbers

sum = num1 + num2 + num3
print(sum)

# The first number minus the second number

sub = num1 - num2
print(sub)

# The third number multiplied 
# by the first number

multiply = num3 * num1
print(multiply)

# The sum of all 
# three numbers divided by the third number

final = sum / num3
print(final)
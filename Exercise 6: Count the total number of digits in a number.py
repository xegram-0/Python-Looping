# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop.

# For example, the number is 75869, so the output should be 5.
number:int = int(input("Enter number: "))
count:int = 0
# for digit in number:
#     count += 1
while number != 0:
    number = number // 10
    count += 1
print("The number of digits is", count)

# Negative numbers do not work
# != would include the single digits
# for loop is the way
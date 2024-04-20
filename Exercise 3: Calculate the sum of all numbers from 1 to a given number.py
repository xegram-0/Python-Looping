# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Expected Output:

# Enter number 10
# Sum is:  55

num = int(input("Enter number: "))
sum = 0
for i in range(num+1):
    sum += i
print("Sum is", sum)

# n = int(input("Enter number "))
# # pass range of numbers to sum() function
# x = sum(range(1, n + 1))
# print('Sum is:', x)
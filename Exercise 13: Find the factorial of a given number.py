# Exercise 13: Find the factorial of a given number
# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120

# Expected output:

# 120

# import math

# factorial_num = int(input("Enter the base number: "))
# print("The result", math.factorial(factorial_num))

factorial_num = int(input("Enter the base number: "))
# Factorial need to be positive
# For now we pass this
result = 1
for i in range(1,factorial_num+1):
    result = result * i
print("The result", result)
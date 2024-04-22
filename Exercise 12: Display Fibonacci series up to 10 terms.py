# Exercise 12: Display Fibonacci series up to 10 terms
# Expected output:

# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

def fibonacci(num):
    first_num = 0
    second_num = 1
    result = 0
    for i in range(num):
        # Print only 1 number at a time
        print(first_num)

        result = first_num + second_num
        #print(result)
        first_num = second_num
        second_num = result
    print("The end.")

num = int(input("How many numbers in fibonacci: "))
fibonacci(num)

# Recursive
# def fibonacci_2(num):

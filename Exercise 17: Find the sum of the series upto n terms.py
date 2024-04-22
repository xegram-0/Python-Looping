# Exercise 17: Find the sum of the series upto n terms
# Write a program to calculate the sum of series up to n term.
# For example, if n =5 the series will become 
# 2 + 22 + 222 + 2222 + 22222 = 24690

# Given:

# # number of terms
# n = 5

# Expected output:

# 24690

def the_sum(number:int):
    baseNum:int = 2
    result:int = 0
    for i in range(number):
        if i < (number):
            print(f"{baseNum}",end=" + ")
        else:
            print("=")
        
        
        result = result + baseNum
        baseNum = baseNum*10 + 2
        
    print(f"The result is {result}")

def main():
    if __name__=="__main__":
        number:int = int(input("Input number: "))
        the_sum(number)

main()
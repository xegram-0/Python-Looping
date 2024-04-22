# Exercise 14: Reverse a given integer number
# Given:

# 76542

# Expected output:

# 24567

def reverse_int(num:int):
    # reverse_num:list = []
    # original_num:str = str(num)
    # for digit in original_num:
    #     reverse_num.append(digit)
    # reverse_num.reverse()
    # print("The reverse is",reverse_num)

    reverse_num = 0
    remainder = 0
    original_num = num
    while original_num > 0:
        remainder = original_num % 10
        reverse_num = reverse_num*10 + remainder
        original_num = original_num // 10
    return reverse_num


def main():
    if __name__=="__main__":
        num = int(input("Enter number: "))
        print("The reversed number is",reverse_int(num))

main()
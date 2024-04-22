# Exercise 15: Use a loop to display elements 
# from a given list present at odd index positions

# Given:

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Note: list index always starts at 0

# Expected output:

# 20 40 60 80 100

def insert_list():
    num = int(input("How many numbers: "))
    originalList:list = []
    for num in range(num):
        originalList.append(int(input("Enter the number: ")))
    
    #print(originalList)
    
    return originalList

def odd_List(originalList):
    
    oddList:list = []

    # This is if outputing the odd number
    # for num in originalList:
    #     if num%2 != 0:
    #         oddList.append(num)

    for i in range(1, len(originalList),2):
        # This displays the indexes of numbers.
        #oddList.append(i)
        oddList.append(originalList[i])

    print(oddList)
def main():
    if __name__=="__main__":
        the_list:list = insert_list()
        odd_List(the_list)
main()
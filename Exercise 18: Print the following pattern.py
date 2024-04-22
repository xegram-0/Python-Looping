# Exercise 18: Print the following pattern

def print_the_expression(rows):

    # # The easy way
    # print("*")
    # print("* *")
    # print("* * *")
    # print("* * * *")
    # print("* * * * *")
    # print("* * * *")
    # print("* * *")
    # print("* *")
    # print("*")

    for i in range(rows):
        for j in range(i):
            print("*", end=" ")
        print("\t")
    for i in range(rows):
        for j in range(rows,i,-1):
            print("*",end=" ")
        print("\t")

def main():
    if __name__=="__main__":
        rows:int = int(input("Input max number of star rows: "))
        print_the_expression(rows)

main()
# Exercise 16: Calculate the cube of 
# all numbers from 1 to a given number

# Given:

# input_number = 6

# Expected output:

# Current Number is : 1  and the cube is 1
# Current Number is : 2  and the cube is 8
# Current Number is : 3  and the cube is 27
# Current Number is : 4  and the cube is 64
# Current Number is : 5  and the cube is 125
# Current Number is : 6  and the cube is 216

def cube_the_number(number):

    for i in range(1, number+1):
        baseNum = i
        cubeNum = i**3
        print(f"Current number is {baseNum} and the cube is {cubeNum}")

def main():
    if __name__=="__main__":
        number = int(input("Input number: "))
        cube_the_number(number)

main()
# Exercise 11: Write a program to display all prime numbers within a range
# Given:

# # range
# start = 25
# end = 50

# Expected output:

# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47

# USING FOR ELSE!!!!!

start = 25
end = 50
primeList : list = []

for num in range(start, end+1):
    if num >1:
        for j in range(2,num):
            if (num%j) == 0:
                break
        else:
                #primeList.append(i)
                print(num)

# listA: list =[]
# listB: list = []

# for i in range(start,end):
#     for j in range(2,i):
#         listA.append(j)
#         listB.append(j)
#         listB.reverse()
#     for k in range(len(listA)):
#         if listA[k]*listB[k] == i:
#             break
#         else:
#             #primeList.append(i)
#             print(i)
#print(listA)
#print(listB)

#print(primeList)



# # Solution:
# start = 25
# end = 50
# print("Prime numbers between", start, "and", end, "are:")


# for num in range(start, end + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num)
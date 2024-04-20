# Exercise 8: Print list in reverse order using a loop

# Given:

# list1 = [10, 20, 30, 40, 50]

# Expected output:

# 50
# 40
# 30
# 20
# 10

list1 = [10, 20, 30, 40, 50]
list2: list = []
#list2 = reversed(list1)
for i in range(len(list1)):
    list2 = list1[::-1]
    #list2.append(list1)
for i in range(len(list2)):
    print(list2[i])

# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i])
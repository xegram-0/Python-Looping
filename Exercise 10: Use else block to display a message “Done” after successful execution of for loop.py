# Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# For example, the following loop will execute without any error.

# Given:

# for i in range(5):
#     print(i)

# Expected output:

# 0
# 1
# 2
# 3
# 4
# Done!

# choice:bool = bool(input("Enter anything: "))
# if choice:
#     print("Not executing else block.")
# else:
#     for i in range(5):
#         print(i)
#     print("Done!")

for i in range(5):
    print(i)
else:
    print("Done!")
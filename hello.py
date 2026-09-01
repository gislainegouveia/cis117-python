# This is my first Python programming assignment
# Author: Gislaine Pires
# Date: 8/31/2026

name = input("What is your name? ")
print("Hello,", name)
my_id = 1377953

print(f"{my_id:08d}")
print(f"{my_id:.2f}")
print(f"{my_id:b}")
print(f"{my_id:#x}")

first = my_id // 10 ** (len(str(my_id)) - 1)
last = my_id % 10

print(first + last)

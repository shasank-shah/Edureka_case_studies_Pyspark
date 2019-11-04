import sys
from time import gmtime, strftime
import math

# 1. What is the output of the following code?
# nums = set([1,1,2,3,3,3,4,4])
# print (len(nums))
# Hint: Set consists unique element.
nums = set([1, 1, 2, 3, 3, 3, 4, 4])
print(len(nums))  # 4

# 2. What will be the output?
d = {"john": 40, "peter": 45}
print(list(d.keys()))  # ['john', 'peter']

# 3. A website requires a user to input username and password to register. Write a program
# to check the validity of password given by user. Following are the criteria for checking password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 3. At least 1 letter between [A-Z]
# 4. At least 1 character from [$#@]
# 5. Minimum length of transaction password: 6
# 6. Maximum length of transaction password: 12
_3InputPassword = input("Enter password: ")
_3Password = []
if len(_3InputPassword) < 6:
    print("Minimum length of password should 6")
    sys.exit(0)
if len(_3InputPassword) > 12:
    print("Maximum length of password should 12")
    sys.exit(0)
for index in _3InputPassword:
    _3Password.append(index)
print(_3Password)

# 4. Write a for loop that prints all elements of a list and their position in the list.
a = [4, 7, 3, 2, 5, 9]
for index in range(len(a)):
    print("index is: ", index, " and element is: ", a[index])

# 5. Please   write   a   program   which   accepts  a   string   from   console   and   print   the
# characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld
_5Input = input("Enter string: ")
_5List = list(_5Input)
_5OutputList = []
_5OutputList.append(_5List[0])
_5Output = ''
for index in range(1, len(_5List)):
    if (index % 2 == 0):
        _5OutputList.append(_5List[index])
print(_5Output.join(_5OutputList))

# 6. Please write a program which accepts a string from console and print it in reverse order.
# Example: If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir

from functools import reduce

def sum(a, b):
    return a*b

list1 = [1, 2, 3, 4, 5]
print(reduce(sum, list1))
# map: it applies some operation within all elements of a list

def double(x):
    return 2*x

list1 = [1, 2, 3, 4]
print(list(map(double, list1)))

# using lambda
print(list(map(lambda x: x**2, list1)))
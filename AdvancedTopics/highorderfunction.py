#A higher-order function is a function that takes another function as an argument or returns a function as its resultss


#map(function, iterable)


numbers = [x for x in range(2, 12, 2)]
print(numbers)



squared_num = list(map(lambda x: x**2 if x>2 else x, numbers))

print(squared_num)


#filter function helps to filter the iterable based on certain conditions

#less than 50

less_than_50 = list(filter(lambda x: x < 50, squared_num))
print(less_than_50)


# reduce helps to aggregate all items into a single value it is present in functools
#reduce(function, iterable, initializer(optional))

from functools import reduce

total = reduce(lambda x, y: x+y, less_than_50)
print(total)






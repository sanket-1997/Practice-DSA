arr = [x for x in range(1,100,10)]
print(arr)

print(arr[1:-2])

print(arr[::-2])


print(arr[:2])

print(arr[2:])



result = lambda x,y: x+y

print(result(20,10))



result = map(lambda x: x**2, arr)

print(list(result))
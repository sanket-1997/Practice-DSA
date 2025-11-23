arr = [1, 2, 3, 4, 5]



def left_rotate(arr):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    
    arr[len(arr)-1] = temp
    return arr


print(left_rotate(arr))




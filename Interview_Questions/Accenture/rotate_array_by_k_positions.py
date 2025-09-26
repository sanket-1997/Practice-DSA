#slicing basics

a = [x+10 for x in range(10)]

print(a)
print(a[2:])
#print(a[2:5:2]) # a[start:end:step]
#print(a[-3:])
#print(a[:-3])


def right_rotate_array(arr, k):
    n = len(arr)
    k = k%n
    arr = arr[-k:] + arr[:-k]

    return arr

def left_rotate_array(arr, k):
    n = len(arr)
    k = k%n
    arr = arr[k:] + arr[:k]

    return arr



print(right_rotate_array(a,12))
print(left_rotate_array(a,2))


#right rotation






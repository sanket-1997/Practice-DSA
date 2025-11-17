def binary_search(arr, element):
    low = 0
    high = len(arr)-1
    mid = (low + high)//2


    while low <= high:
        if element > arr[mid]:
            low = mid+1
        elif element < arr[mid]:
            high = mid-1
        else:
            return mid

        mid = (low+high)//2
   
    
    return -1

arr = [10, 20, 30, 34, 45, 90]
element = 90

print(binary_search(arr, element))




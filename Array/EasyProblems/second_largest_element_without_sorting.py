def second_largest(arr):
    largest = -1
    s_largest = -1
    n = len(arr)

    for i in range(n):
        if arr[i] > largest:
            largest = arr[i]

    for i in range(n):
        if arr[i] > s_largest and arr[i] < largest:
            s_largest = arr[i]
        
    
    return s_largest

arr = [9,10, 0, 2, 9, 21, 3, 5]
arr2 = [7,7,7,7]

print(second_largest(arr2))

#Time Complexity = O(N + N)
#Space Complexity = O(1)

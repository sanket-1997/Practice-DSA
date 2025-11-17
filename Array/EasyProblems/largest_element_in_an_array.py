


def largest_element(arr):
    max = 0

    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    
    return max



arr = [9,10, 0, 2, 9, 21, 3, 5]

print(largest_element(arr))

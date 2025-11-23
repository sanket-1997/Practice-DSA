#brute solution



def left_rotate_array_d_places(arr: list, d: int) -> list:
    length_of_array = len(arr)
    effective_rotation = d % length_of_array

    if effective_rotation == 0:
        return arr

    temp = arr[:effective_rotation] # o(effective_rotation)

    for i in range(effective_rotation, length_of_array):   # o(length_of_array - effective_rotation)
        arr[i - effective_rotation] = arr[i]
    
    for i in range(len(temp)): #o(effective_rotation)
        arr[length_of_array - effective_rotation + i] = temp[i]
    
    return arr

def left_rotate_array_d_places_optimal(arr: list , d: int) -> list:
    effective_rotation = d% len(arr)
    arr = arr[effective_rotation:] + arr[:effective_rotation]

    return arr

print(left_rotate_array_d_places([1,2,5,6,3,4], 2))

#Time Complexity = O(effective_rotation) + O(length_of_array - effective_rotation) + O(effective_rotation)
#Space Complexity = O(effective_rotation)





print(left_rotate_array_d_places([1,2,5,6,3,4], 2))

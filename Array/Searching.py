array = [10,20,30,5, 2, 100]

sorted_array = [7, 10, 20, 35, 50, 89 ,100, 112, 115, 120, 150, 670, 1000]


#Linear Search
print("Linear Search")
element = 100
bool = False
for i in range(len(array)):
    if element == array[i]:
        print(f'Found element {element} at position {i}')
        bool = True
        break

if not bool:
    print("Not Found")




print("\n\n\n")
#Binary Search

low = 0
high = len(sorted_array)-1
bool2 = False

print("Binary Search")

while low<= high:
    mid = (low + high)//2
    if sorted_array[mid] == element:
        print(f'Found element {element} at position {mid}')
        bool2 = True
        break
    elif element > sorted_array[mid]:
        low = mid + 1
    else:
        high = mid - 1


if not bool2:
    print('Not Found')
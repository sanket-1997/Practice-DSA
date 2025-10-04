nums = [x for x in range(10, 90, 10)]
print(nums)

#get first 3 elemets
print(nums[:3])
#get last 2 elements
print(nums[-2:])
#get everything except the first element
print(nums[1:])
#get everything except the last element
print(nums[:-1])
#copy entire list using slicing
copy = nums[::]
print(copy)

#get every 2nd element
print(nums[::2])
#get elements from index 2 to 6
print(nums[2:7])
#get elements from index 1 to 6 with step 2
print(nums[1:7:2])
#reverse the list
print(nums[::-1])
#get the last 3 elements in reverse
print(nums[:4:-1])

#get all except the first and last element
print(nums[1:7])
#get middle 4 elements
#print(nums[?])
arr = [1, 2, 3,1, 1,10,5, 9, 50, 10, 10, 0, 1]


frequency ={}


for number in arr:
    if number in frequency:
        frequency[number] +=1
    else:
        frequency[number] = 1



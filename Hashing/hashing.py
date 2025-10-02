#basic concept is to create a hashmap in order to create kind of memory

s = "aabcccd"

frequency ={}

for ch in s:
    if ch in frequency:
        frequency[ch] +=1
    else:
        frequency[ch] =1

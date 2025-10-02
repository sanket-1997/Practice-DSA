#abaacdddda -> 4ab1c1d4



s = "abaacdddda"

hashmap = {}


for i in range(len(s)):
    if s[i] in hashmap:
        hashmap[s[i]] +=1
    else:
        hashmap[s[i]] =1

print(hashmap)




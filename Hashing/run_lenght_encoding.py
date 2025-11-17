#abaacdddda -> 4ab1c1d4



s = "abaacdddda"


hashmap2 = {}

for ch in s:
    if ch in hashmap2:
        hashmap2[ch] +=1
    else:
        hashmap2[ch] =1

s=""
for ch in hashmap2:
    s=s+ch+str(hashmap2[ch])

print(s)




hashmap = {}


for i in range(len(s)):
    if s[i] in hashmap:
        hashmap[s[i]] +=1
    else:
        hashmap[s[i]] =1

print(hashmap)




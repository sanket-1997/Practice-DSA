s= "cadbzabcdef"
n= len(s)

#use hashvalue substring = 2 pointer

hash = {}

l,r,max_length = 0,0,0

#print(l,r, max_length)

while(r<n):
    if s[r] in hash:
        if (hash[s[r]]>=l):
            l = hash[s[r]]+1
    len = r-l+1
    max_length = max(len, max_length)
    hash[s[r]] = r
    r +=1


print(max_length)
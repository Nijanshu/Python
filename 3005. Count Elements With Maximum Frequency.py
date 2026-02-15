# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.

nums = [10,12,11,9,6,19,11]

freq={}

for i in nums:
    if i in freq:
        freq[i]+=1
        continue
    freq[i]=1

print(freq)
maxx=0
tmax=0

for i in freq.values():
    
    maxx=max(maxx,i)


ff=0
for f in freq.values():
    if f==maxx:
        ff+=1

print(ff*maxx)
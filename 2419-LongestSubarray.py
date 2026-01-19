def longestSubarray(nums):
    m=max(nums)
    longest=0
    c=0

    for i in nums:
        if i==m:
            c+=1
            longest=max(longest,c)
        else:
            c=0
        
    return longest

print(longestSubarray([1,2,4,4,3,3,2,4,2]))


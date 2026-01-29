# Given an array nums, you can perform the following operation any number of times:

# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.

# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).

nums=[260,-203,241,495,554,-174,476,-574,531,-526,-518,14,-541,24,606,-394,-515,103,413,565,426,-295,682,366]


def minimumPairRemoval(nums):
    asc=True
    # if(len(nums)<=1): return 0
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            asc=False
            break
    
    if asc==True: return 0
    pairs=[(nums[i],nums[i+1])  for i in range(len(nums)-1)]
    print("p=",pairs)
    min=10**9

    for j in range(len(nums)-1):
        s=nums[j]+nums[j+1]
        if s<min:
            min=s
            min_index=j

    nums.pop(min_index)
    nums.pop(min_index)
    print("min =",min)

    nums.insert(min_index,min)
    print("s=",s,nums)

   
    return 1+minimumPairRemoval(nums)


print(minimumPairRemoval(nums))
    

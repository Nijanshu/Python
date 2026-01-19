#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#You can return the answer in any order.

def twoSum(nums, target):
    for i in range(0,len(nums)):
        for j in range(0,len(nums)):
            if(i!=j):
                if nums[i]+nums[j] == target:
                    return [i, j]


numbers=[2,7,11,15]
target=22
print(twoSum(numbers, target))

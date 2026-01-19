def removeElement(nums:list[int], val):
    i=0
    while i in range(len(nums)):
        print(nums[i])
        if(nums[i] == val):
            nums.remove(nums[i])
        else:
            i+=1

    # print(f"Array: {nums}")
    k=len(nums)
    return k

nums= [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(nums, val))


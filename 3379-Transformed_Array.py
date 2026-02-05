nums = [3,-2,1,1]
l=len(nums)
res=[]

for i in range(len(nums)):
        res.append(nums[i+nums[i]%l] if i+nums[i]%3<l else nums[i+nums[i]%l-l])
  

print(res)
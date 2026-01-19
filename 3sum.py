#LEETCODE 15

def threeSum(nums):
    l:list=[]
    for i in range(len(nums)):

        for j in range(len(nums)):
            if(i!=j):
                for k in range(len(nums)):
                    if(k!=i and k!=j):
                        if(nums[i]+nums[j]+nums[k]==0):
                            b=[nums[i],nums[j],nums[k]]
                        
                            l.append(b)
                            print(l)
                            if(len(l)>1):
                                for x in range(len(l)-1):
                                    n=0
                                    for y in range(len(l[x])):
                                        for z in range(len(b)):
                                            if l[x][y]==b[z]:
                                                n+=1
                                                break
                                            # break
                                            # else:
                                            #     break
                                            
                                    print(n)
                                    if(n==3):
                                        # if([0,0,0] in l):
                                        #     break
                                        l.pop()
                                        print(f"updated list:{l}")
    return f"final list:{l}"

nums = [0,0,0,-1,1]
print(threeSum(nums))

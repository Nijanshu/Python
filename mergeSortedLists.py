def mergeTwoLists(list1, list2):
    list1.extend(list2)
    list1.sort()
    return list1

def remove_duplicates(nums):
    i=0
    lenn=len(nums)
    while i<len(nums)-1:
        if(nums[i] == nums[i+1]):
            print (f"duplicate: {nums[i]}")
            nums.pop(i)
            # list.append('_')
        else:
            i+=1
    # for k in range(i+1, lenn):
    #     nums.append('_')
    #     # nums[k]='_'
    print(len(nums))          

list1 = [1,2,2,2,2,3,6,6,6,7,7,7]
list2 = [1,1,2]
# print(mergeTwoLists(list1,list2))

remove_duplicates(list2)
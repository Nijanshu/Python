#Write a function to find the longest common prefix string amongst an array of strings.

'''If there is no common prefix, return an empty string '''


def commonintwo(str1, str2):
    l1=len(str1)
    l2=len(str2)
    common=''
    for i in range(min(l1,l2)):
        if str1[i]==str2[i]:
            common+=str1[i]
        else:
            return common
    return common

# def find_common_prefix(strs):
#     strr=[]
#     for i in range(len(strs)):
#         if(i<len(strs)-1):
#             c1= commonintwo(strs[i],strs[i+1])
#             strr.append(c1)

#     print(strr)
#     print(len(strr))
#     if(len(strr)==1):
#         print("oka")
#         return (f'{strr} okay')
    
#     find_common_prefix(strr)

     
# def find_common_prefix(strs):
#     if not strs:
#         return ""
    
#     # Start with the first string as the initial common prefix
#     prefix = strs[0]
    
#     # Compare the prefix with each subsequent string
#     for i in range(1, len(strs)):
#         prefix = commonintwo(prefix, strs[i])
        
#         # If the common prefix becomes empty, there's no common prefix
#         if not prefix:
#             return ""
    
#     return prefix     

def find_common_prefix(strs):
    strs=sorted(strs)
    common=''
    # first
    for i in range(min(len(strs[0]),len(strs[-1]))):
        if strs[0][i] == strs[-1][i]:
            common+=strs[0][i]
        else:
            return common

    return common

strs=["preheat","oven","prehistoric"]
print(sorted(strs))

print(find_common_prefix(strs))
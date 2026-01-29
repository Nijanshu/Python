# Given an array arr[] of unique elements. Generate all possible permutations of the elements in the array.
# Note: You can return the permutations in any order, the driver code will print them in sorted order.

# Examples:

# Input: arr[] = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
# Explanation: There are 6 possible permutations (3! = 6) of the array.
# Input: arr[] = [1, 3]
# Output: [[1, 3], [3, 1]]
# Explanation: There are 2 possible permutations (2! = 2) of the array.

arr=[1,2,3]
l=len(arr)
p=1
for i in range(1,len(arr)+1):
    p*=i

perms=[0,0,0]

for i in range(p):
    perms[i]=list(perms[i])
    for j in range(l):
        perms[i].append(j)

print(perms)
    

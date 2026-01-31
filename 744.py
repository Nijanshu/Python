# You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

# Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

letters = ["x","x","y","y"]
target = "z"

t=ord(target)

# l=1000

# for i in letters:
#     if t!=ord(i):
#         print(target,i)
#         if ord(i)>t and ord(i)<=l:
#             l=ord(i)

# if(l==1000):
#     print(letters[0])
# else:               
#     print (chr(l))


l="}"

for i in letters:
    if target!=i:
        if i>target and i<=l:
            l=i

if(l=="}"):
    print(letters[0])
else:
    print(l)
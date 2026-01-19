str1=input("Enter string1: ")
str2=input("Enter string2: ")

str1=str1.replace(" ","")
str2=str2.replace(" ","")

ar1=list(str1)
ar2=list(str2)

l1=ar1.sort()
l2=ar2.sort()

print(ar1)
print(l1)
print(ar2)
print(l2)

if(l1==l2):
    # for i in str1:
    #     if i not in str2:
    #         print("Not anagram")
    #         break
    
    print("Anagram")

# def palindrome(num):
#     num=str(num)
#     print(type(num))
#     if(num==num[::-1]):
#         return("Palindrome")
    
#     else:
#         return("Not a Palindrome")
        

    # for i in range(len(num)//2):
    #     if num[i]!=num[-i-1]:
    #         return("Not palindrome")
    

def palindrome(num):
    on=num
    arr=[]
    while(num>0):
        rem=num%10
        num=num//10
        arr.append(rem)
    print(arr) 
    print(len(arr)) 
    arr.reverse()
    print(arr) 
    n2=0
    for i in range(len(arr)):
        n2+=arr[i]*(10**i)
   
    if(n2==on):
        return("Palindrome")
    else:
        return("Not palindrome")

number=input("Enter a number")
number=int(number)
print(palindrome(number))

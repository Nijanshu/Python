import random

# n= random.randint(2,11)

def fib(n):  #no. at nth pos

    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fibseries(n):  
    arr=[]
    for i in range(1,n+1):
        arr.append(str(fib(i)))
    a=' '.join(arr)
    print (a)




def sumfib(n):  # sum of fibbonacci sequences upto nth pos
    if(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return sumfib(n-1)+fib(n)
    
# print('Random number:', n)
n=int(input('Enter the length of fibonacci sequence'))
print(f"{n}th digit is",fib(n))
# print("sum:",sumfib(n))

fibseries(n)
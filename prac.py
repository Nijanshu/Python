# name= input("Enter your name: ")
# roll_no= input("Enter your roll number: ")
# age=input("Enter your age: ")
# roll_no=int(roll_no)
# age=int(age)

# print("Name:",name,"\n","Age: ",age,"\n","roll no:",roll_no, "\n") 
 
# print(f"Hello {name} your roll no is {roll_no} and you're {age} years old")

# def fib(n):
#     a,b=0,1
#     sum=0

#     for i in range(n):
#         a,b=b,b+a
#         sum=sum+a
#         if(i%2==0):
#             continue
#         print(a, end=" ")
    
#     print("\nSum of terms is", sum)
        
        


# n=int(input("Enter number of terms: "))
# fib(n)


# def swap(a,b):
#     a,b=b,a
#     print("a=",a)
#     print("b=",b)

# swap(2,3)

def pattern(n):
    for i in range(n):
        # print()
        print(((i))*" "+(n-i)* f"{n-i} ")

pattern(55)

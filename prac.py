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

# def pattern(n):
#     for i in range(n):
#         # print()
#         print(((i))*" "+(n-i)* f"{n-i} ")

# pattern(55)


def resolution_streak(days):
    walk=10000
    screen=120
    pages=5

    print(days[0])
    for i,day in enumerate(days, start=1):
        print(day[1])
        if day[0]<walk:
            return f"Resolution failed on day {i}:{i-1} day streak."
        if day[1]>screen:
            return f"Resolution failed on day {i}:{i-1} day streak."
        if day[2]<pages:
            return f"Resolution failed on day {i}:{i-1} day streak."
        
    return f"Resolution on track: {len(days)} day streak."

print(resolution_streak([[10000, 120, 5], [10950, 121, 11]]))
    
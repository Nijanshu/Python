# a=input("Enter your age")
# b=input("Enter your name")
# a=int(a)
# print(a*2,b[-1])
# print(b.swapcase())

# for x in 'range (0,a)'.center(20):{
#     print(x)
# }


from datetime import datetime 

now = datetime.now() # current date and time

hrs = int(now.strftime("%H"))
print("time:", type(hrs))
if(hrs<12 and hrs>4):
    print('Good Morning')
elif(hrs>12 and hrs<16):
    print('Good Afternoon')
elif(hrs>16 and hrs<20):
    print('Good Evening')
else:
    print('Good Night')

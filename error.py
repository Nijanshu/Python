a= input("Enter a number between 5 and 10 ")

if (a=="quit"):
    pass
elif(int(a)<5 or int(a)>10):
    raise ValueError("Please enter a number between 5 and 10")
else:
    print("okay")


import random

def sps():
    ls=["stone","paper","scissors"]
    comp=random.randint(0,2)

    inp=input("Enter your choice")

    print(ls[comp])
    matrix = [[0,-1,1], 
        [1,0,-1],
        [-1,1,0]]


    if(inp.lower()=="stone"):
        final=matrix[0][comp]
    elif(inp.lower()=="paper"):
        final=matrix[1][comp]
    elif(inp.lower()=="stone"):
        final=matrix[2][comp]
    else:
        print ("Invalid input")
        return 

    print(final)
    if(final==-1):
        print("You lose")
    elif(final==1):
        print("You won")
    else:
        print("Draw")

sps()
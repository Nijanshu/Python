# from decToBin import decToBinary 

def minBitFlips(start, goal):
    def decToBinary(d):
        b=0
        i=0
        while(d>0):
            b+=10**(i)*(d%2)
            d=d//2
            i+=1

        return b
    start = str(decToBinary(start))
    goal = str(decToBinary(goal))

    if(len(start)>len(goal)):
        goal='0'*(len(start)-len(goal))+goal
    else:
        start='0'*(len(goal)-len(start))+start

    steps=0
    for i in range(len(start)):
        if(start[i]!=goal[i]):
            steps+=1
    
    return steps

print(minBitFlips(7,10))

     



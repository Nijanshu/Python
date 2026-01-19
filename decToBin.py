def decToBinary(d):
    b=0
    i=0
    while(d>0):
        b+=10**(i)*(d%2)
        d=d//2
        i+=1

    return b

def bintoDec(b):
    d=0
    i=0
    while(b>0):
        d+=2**i*(b%10)
        b=b//10
        i+=1
    return d


print(bintoDec(1100)) 
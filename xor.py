from decToBin import decToBinary
def xor(a,b):
    a=str(decToBinary(a))
    b=str(decToBinary(b))
    v=0
    for i in range(len(a)):
        if(a%10!=b%10):
            v+=10**i
        else:
            print('same')

    return v

xor(4,5)

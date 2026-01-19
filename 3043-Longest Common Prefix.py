def prefix(n1,n2):
    n1=str(n1)
    n2=str(n2)
    s=0

    for i in range(len(min(n1,n2))):
        if(n1[i]==n2[i]):
            s+=1
        else:
            return s

    return s


# def prearray(arr1,arr2):
#     l=0
#     for i in range(len(arr1)): 
#         for j in range(len(arr2)):
#             if prefix(arr1[i],arr2[j])>l:
#                 l=prefix(arr1[i],arr2[j])
        
#     return l


def prearray(arr1,arr2):
    maxm=0
    for i in range(len(arr1)): 

        for j in range(len(arr2)):
            n1=max(arr1[i],arr2[j])
            n2=min(arr1[i],arr2[j])
            s=0
            while(n2>=1):
                if(n1/(10**(len(str(n1))-1))==n2/(10**(len(str(n2))-1))):
                    s+=1
                    print("s = ",s)
                    n1=n1/10
                    n2=n2/10
                else:
                    break
            if(s>maxm):
                maxm=s
                
    return maxm


print(prearray([1,10,1000],[100,200,34]))


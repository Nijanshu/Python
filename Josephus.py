def josephus(n, k):

    # code here
    killed=[]
    next=k
    
    while(len(killed)!=n-1):
        if(next not in killed):
            killed.append(next)
        else:
            next+=1
        next+= k if next+k<n else k-n
        
    print(killed)

    for i in range(1,n+1):
        if i not in killed:
            print(i)
        
n = 5
k = 2

josephus(n,k)
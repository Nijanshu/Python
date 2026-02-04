def josephus(n, k):

    # code here
    killed=[i for i in range(1,n+1)]
    next=k
    
    while(len(killed)!=n-1):
        if(next in killed):
            killed.pop(killed[next])
        l=len(killed)
        next+= k if next+k<n else k-n
        
    print(killed)

    for i in range(1,n+1):
        if i not in killed:
            print(i)
        
n = 5
k = 2

josephus(n,k)
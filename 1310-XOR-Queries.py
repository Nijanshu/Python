from decToBin import decToBinary, bintoDec
def xorQueries(arr, queries):
    d=[]
    for i in arr:
        d.append(i)
    
    print(d)
    l=[]
    for j in queries:
        v=d[j[0]]
        print(v,j)
        for k in range(j[0],j[1]):
            v=v^d[k+1]
            print(d[k],d[k+1],v)

        l.append(v)     

    return l


arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(xorQueries(arr, queries))







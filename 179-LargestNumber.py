def largestNumber(nums):
    l=[]
    for i in nums:
        i=str(i)
        l.append(i)
    # l=list(int(l))
    for k in l:
        k=int(k)
        m=max(l)
        print(m)
    print(l)
    
    l.sort(key=lambda s:s*10,reverse=True)
    print(l)
    v=''.join(l)
    if v[0]=='0':
        v='0'
    # v=reversed(v)
    return v

print(largestNumber([0,0]))

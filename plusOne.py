#LEETCODE 66

def plusOne(digits:list):
    s= int(''.join(map(str,digits)))
    print(s)
    a=s+1
    a=str(a)
    l=[]
    for i in a:
        l.append(int(i))
    
    return l

digits=[9]
print(plusOne(digits))

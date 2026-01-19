def addBinary(a,b):
    s=''
    carry='0'
    if(len(a)>len(b)):
        b='0'*(len(a)-len(b))+b
    else:
        a='0'*(len(b)-len(a))+a
     
    for i in range(1,len(a)+1):
        
        if a[-i] == b[-i] and a[-i]=='1':
            s+=carry
            carry='1'
        elif a[-i] == b[-i] and a[-i]=='0':
            s+=carry
            carry='0'
        elif a[-i] != b[-i]:
            print("no")
            if(carry=='0'):
                s+='1'
            if(carry=='1'):
                s+='0'
    if(carry=='1'):
        s+=carry
    s=s[::-1]
    return s


print(addBinary('100','1'))
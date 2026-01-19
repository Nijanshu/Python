def parentheses(exp):
    l=[]
    for i in exp:
        l.append(i)
    
    print(l)
    v="".join(l)
    v=int(v)
    print(v)

        

parentheses("2-2-1")
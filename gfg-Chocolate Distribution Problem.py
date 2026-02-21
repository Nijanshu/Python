arr = [3, 4, 1, 9, 56, 7, 9, 12]
m = 5
sub=[]

for i in range(m):
    sub.append(i)
    for j in arr:
        sub.append(i+1)
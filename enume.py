x = ('apple', 'banana', 'cherry')
y = enumerate(x,1)

print(list(y))

for i,val in enumerate(x,1):
    if i==1:
        print(val,'thanks')
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 2, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        # break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

f=open("lists.py", "r")

for x in f:
    w=x.strip()
    a=w.split(' ')
    print(a)
    for i in a:
        if("print" in i):
            print(i)
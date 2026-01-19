# i=0

for i in range(20):
    if(i%2 != 0):  # check even numbers and skip
        continue
    if(i>10):  # keep range to 10
        break
    print(i)
arr = [3, 30, 34, 5, 9]
from functools import cmp_to_key


arr2=[]
for i in arr:
    print(type(i))
    i=str(i)
    arr2.append(str(i))
    print(type(i))

print(arr2)
print(type(arr2[2]))

def compare(a, b):

        if a + b > b + a:

            return -1 # a before b

        elif a + b < b + a:

            return 1 # b before a

        else:

            return 0

arr2.sort(key=cmp_to_key(compare))
print(arr2,"".join(arr2))
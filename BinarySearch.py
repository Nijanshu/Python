arr=[6, 12, 14, 18, 22, 39, 55, 182]
target=20


def binSearch(arr,target):
    l=len(arr)
    if arr[l//2]==target:
        print("found at pos:", l//2)
        return
    if(l==1):
        print("Not found")
        return
    elif arr[l//2]<target:
        print(f"{arr[l//2]} more")
        binSearch(arr[l//2+1:],target)

    elif arr[l//2]>target:
        print(f"{arr[l//2]} less")
        binSearch(arr[:l//2],target)

    

binSearch(arr,target)
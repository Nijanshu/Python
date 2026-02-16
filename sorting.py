def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):

            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]


def selectionSort(arr,k):
        
    for i in range(len(arr)-1):
        smallest=min(arr[i:])
        sid=arr[i:].index(smallest)
        arr[i+sid],arr[i]=arr[i],arr[i+sid]

        
        
arr=[3,4,5,1,9,1,2,4]
# bubbleSort(arr)
selectionSort(arr,0)
print(arr)
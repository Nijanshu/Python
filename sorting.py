def bubbleSort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):

            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]


def selectionSort(arr):
        
    for i in range(len(arr)-1):
        smallest=min(arr[i:])
        sid=arr[i:].index(smallest)
        arr[i+sid],arr[i]=arr[i],arr[i+sid]

def insertionSort(arr):
    for i in range(1,len(arr)-1):
        for j in range(i):
            print(arr[i],arr[j])
            if arr[i]<arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
        print(arr)
        
        
        
arr=[3,2,5,1,9,1,2,4]
# bubbleSort(arr)
# selectionSort(arr)
insertionSort(arr)
print(arr)
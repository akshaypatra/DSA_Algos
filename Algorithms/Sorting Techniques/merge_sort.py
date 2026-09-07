'''
Merge Sort : divide and conquer method to divide the arr into half and sorting the halfs repectively and then  
            merging the halfs using merge function that comapres the values from each half put the value .

Time Complexity : O( nlogn )

'''
def merge(left_half,right_half,arr):
    i=j=k=0

    while i<len(left_half) and j<len(right_half):
        if left_half[i]<right_half[j]:
            arr[k]=left_half[i]
            i+=1
        else:
            arr[k]=right_half[j]
            j+=1
        k+=1
    while i<len(left_half):
        arr[k]=left_half[i]
        i+=1
        k+=1

    while j<len(right_half):
        arr[k]=right_half[j]
        j+=1
        k+=1
    return arr


def mergeSort(arr):
    res=arr
    low=0
    high=len(arr)
    if len(arr)>1:

        mid=(low+high)//2
        left_half=arr[:mid]
        right_half=arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        res=merge(left_half,right_half,arr)

    return res


print(mergeSort([3,2,1,7,8,6,4]))
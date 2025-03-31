'''
Insertion Sort :  It builds the sorted array one element at a time by taking an element from the unsorted part and placing it in its correct position in the sorted part.

Time Complexity : O(n^2)

'''

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertionSort([3,2,1,6,7,8,7,3,2]))




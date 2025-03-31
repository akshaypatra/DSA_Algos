'''
Quic Sort algorithm : Divide and Conquer , Pivot
Time Complexity : O(nlogn)

QuickSort algo working :
    To find partition (finds the correct location for pivot i.e everything on left of pivot index are smaller 
                        and on right every element is larger ):

        i=low-1
        j=low
        pivot=arr[high]

        loop :
            if value at j is less than pivot -> ignore the value , j+=1
            if value is less than j -> i+=1 ,swap values of i and j,j+=1
        loop end

        (now we now that i+1 is the final resting place for our pivot)
        i+=1
        swap values at i and j

        return the index i 

    quickSort(arr,low,high)
        if low<high:
            pivot_index =partition(arr,low,high) 
            quickSort(arr,low,pivot_index-1)
            quickSort(arr,pivot_index+1,high)
        return arr

'''
def partition(arr,low,high):
    i=low-1
    j=low
    pivot=arr[high]

    while j<high:
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
        j+=1
    i+=1
    arr[i],arr[j]=arr[j],arr[i]

    return i

    
def quickSort(arr,low,high):

    if low<high:
        pivot_index=partition(arr,low,high)
        quickSort(arr,low,pivot_index-1)
        quickSort(arr,pivot_index+1,high)

    return arr

print(quickSort([3,2,1,6,7,4,5],0,6))
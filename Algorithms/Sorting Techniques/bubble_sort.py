'''
Time Complexity : O(n^2)
'''

def bubbleSort(arr):

    for i in range(len(arr)-1):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
       

    return arr

print(bubbleSort([3,2,1,7,5,6]))
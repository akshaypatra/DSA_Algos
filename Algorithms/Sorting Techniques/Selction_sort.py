'''
Time Complexity : O(n^2)
'''

def selctionSort(arr):
    cur_index=0
    while cur_index<len(arr)-1:
        cur_min=arr[cur_index]
        idx=cur_index
        for i in range(cur_index,len(arr)):
            if arr[i]<cur_min:
                cur_min=arr[i]
                idx=i
        arr[cur_index],arr[idx]=arr[idx],arr[cur_index]
        cur_index+=1
    return arr

print(selctionSort([3,2,1,7,7,6,8,7,4]))

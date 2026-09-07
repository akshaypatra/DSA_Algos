'''
Binary Search Algorithm

1. Divide the search space into two halves by finding the middle index "mid". 
2. Compare the middle of the search space with the key. 
3. If the key is found at middle, the process is terminated.
4. If the key is not found at middle, choose which half will be used as the next search space.
    -> If the key is smaller than the middle, then the left side is used for next search.
    -> If the key is larger than the middle, then the right side is used for next search.
This process is continued until the key is found or the total search space is exhausted.

'''

def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:

        mid = low + (high - low) // 2

        # Check if x is present at mid
        if arr[mid] == x:
            return mid

        # If x is greater, ignore left half
        elif arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        else:
            high = mid - 1

    # If we reach here, then the element
    # was not present
    return -1

if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, x)
    if result != -1:
        print("Element is present at index", result)
    else:
        print("Element is not present in array")
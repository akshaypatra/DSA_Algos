'''
Voting Algorithm 

Use_case : Majority finding problems

How it works :

-> Counts the frequency of majority element
-> while iterating over array , we subtract the count to get remaining elements (in further array)
-> this reduces useage of hashmap.


The voting algorithm commonly used in Data Structures and Algorithms (DSA) is the Boyer-Moore Majority Vote Algorithm.

Boyer-Moore Majority Vote Algorithm
It is used to find the majority element (an element that appears more than ⌊n/2⌋ times) in an array in O(n) time and O(1) space.

Algorithm Steps :

1. Initialize a candidate with an element and a count = 1.
2. Iterate through the array:
    ->If the next element is the same as the candidate, increment count.
    ->If the next element is different, decrement count.
    ->If count becomes 0, change the candidate to the current element and reset count = 1.

The remaining candidate after the loop is the majority element (if it exists).

'''
# Implementation

def majorityElement(nums):
    candidate, count = None, 0

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

# Example Usage
arr = [3, 3, 4, 2, 3, 3, 3]
print(majorityElement(arr))  # Output: 3

'''
Time Complexity: O(n)
Space Complexity: O(1)
This algorithm is efficient and widely used in problems requiring a majority element.

Example : leetcode 2780. Minimum Index of a Valid Split
'''
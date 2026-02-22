"""
binary_toolkit.py

Complete Binary + Bit Manipulation + Binary Search Toolkit

Each function contains:
- Purpose
- Explanation
- Example
- Time Complexity

Perfect for interview prep & revision.

Author: Akshay
"""

# ======================================================
# BITWISE OPERATIONS
# ======================================================

def is_bit_set(n, i):
    """
    Checks whether ith bit is set.

    Example:
    n = 5 (101), i = 0 → True

    Logic:
    Shift 1 to ith position and AND with n.

    Time: O(1)
    """
    return (n & (1 << i)) != 0


def set_bit(n, i):
    """
    Sets ith bit to 1.

    Example:
    5 (101), set bit 1 → 111 (7)

    Time: O(1)
    """
    return n | (1 << i)


def clear_bit(n, i):
    """
    Clears ith bit.

    Example:
    7 (111), clear bit 1 → 101 (5)

    Time: O(1)
    """
    return n & ~(1 << i)


def toggle_bit(n, i):
    """
    Toggles ith bit.

    Example:
    5 (101), toggle bit 0 → 100 (4)

    Time: O(1)
    """
    return n ^ (1 << i)


def count_set_bits(n):
    """
    Counts number of 1s using Brian Kernighan Algorithm.

    Removes lowest set bit each iteration.

    Time: O(number of set bits)
    """
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


def is_power_of_two(n):
    """
    Checks if number is power of 2.

    Property:
    Power of 2 has only one set bit.

    Example:
    16 → True
    18 → False

    Time: O(1)
    """
    return n > 0 and (n & (n - 1)) == 0


def lowest_set_bit(n):
    """
    Returns lowest set bit.

    Example:
    12 (1100) → 4

    Time: O(1)
    """
    return n & -n


def remove_lowest_set_bit(n):
    """
    Removes lowest set bit.

    Example:
    12 (1100) → 8 (1000)

    Time: O(1)
    """
    return n & (n - 1)


def xor_swap(a, b):
    """
    Swaps two numbers using XOR (no temp variable).

    Time: O(1)
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


# ======================================================
# BITMASKING
# ======================================================

def generate_subsets(arr):
    """
    Generates all subsets using bitmasking.

    Total subsets = 2^n

    Used in:
    - Subset problems
    - Bitmask DP

    Time: O(n * 2^n)
    """
    n = len(arr)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result


# ======================================================
# BINARY SEARCH
# ======================================================

def binary_search(arr, target):
    """
    Standard Binary Search.

    Finds index of target in sorted array.

    Time: O(log n)
    """
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def lower_bound(arr, target):
    """
    First index where value >= target.

    Used in:
    - Frequency problems
    - Insert position

    Time: O(log n)
    """
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


def upper_bound(arr, target):
    """
    First index where value > target.

    Time: O(log n)
    """
    l, r = 0, len(arr)
    while l < r:
        mid = (l + r) // 2
        if arr[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l


# ======================================================
# BINARY SEARCH ON ANSWER
# ======================================================

def binary_search_answer(low, high, feasible):
    """
    Used when searching solution space.

    Example:
    - Min capacity
    - Max distance
    - Eating bananas

    Pattern:
    F F F T T T

    Time: O(log range)
    """
    while low <= high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid - 1
        else:
            low = mid + 1
    return low


# ======================================================
# ROTATED SORTED ARRAY SEARCH
# ======================================================

def search_rotated(nums, target):
    """
    Binary search in rotated sorted array.

    Time: O(log n)
    """
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m

        if nums[l] <= nums[m]:
            if nums[l] <= target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1

    return -1


# ======================================================
# PEAK ELEMENT
# ======================================================

def find_peak(nums):
    """
    Finds peak element using binary search.

    Peak:
    nums[i] > nums[i-1] and nums[i] > nums[i+1]

    Time: O(log n)
    """
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] < nums[m + 1]:
            l = m + 1
        else:
            r = m
    return l


# ======================================================
# TEST AREA
# ======================================================

if __name__ == "__main__":
    print("Set bits:", count_set_bits(15))
    print("Power of two:", is_power_of_two(16))
    print("Binary search:", binary_search([1,2,3,4,5], 4))
    print("Lower bound:", lower_bound([1,2,2,2,3], 2))
    print("Upper bound:", upper_bound([1,2,2,2,3], 2))
    print("Subsets:", generate_subsets([1,2,3]))
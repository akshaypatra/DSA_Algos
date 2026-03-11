"""
slow_fast_pointer.py 

Floyd's cycle detection algorithm

This module explains and demonstrates the Slow and Fast Pointer technique
(commonly called the Tortoise and Hare algorithm).

The slow and fast pointer technique is a commonly used algorithmic pattern
for problems involving linked lists, arrays, and cycle detection.

Core Idea
---------
Two pointers traverse a data structure at different speeds.

    slow pointer -> moves 1 step at a time
    fast pointer -> moves 2 steps at a time

Because the fast pointer moves faster, it eventually catches up to the
slow pointer if a cycle exists.

Common Use Cases
----------------
1. Detect cycle in a linked list
2. Find the middle of a linked list
3. Find the start of a cycle
4. Remove the nth node from the end
5. Detect cycles in sequences (e.g., Happy Number)

Advantages
----------
Time Complexity: O(n)
Space Complexity: O(1)

This makes the technique extremely efficient compared to solutions
that require extra memory like hash sets.
"""


class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes
    ----------
    val : int
        Value stored in the node.
    next : ListNode
        Reference to the next node in the list.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_middle(head):
    """
    Find the middle node of a linked list using the slow-fast pointer technique.

    Concept
    -------
    - slow pointer moves one step at a time
    - fast pointer moves two steps at a time
    - when fast reaches the end, slow will be at the middle

    Example
    -------
    Input list:
        1 -> 2 -> 3 -> 4 -> 5

    Movement:
        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=5
        Step 3: fast reaches end

    Result:
        slow points to node with value 3 (middle)

    Parameters
    ----------
    head : ListNode
        Head node of the linked list.

    Returns
    -------
    ListNode
        Middle node of the linked list.

    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(1)
    """

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def has_cycle(head):
    """
    Detect whether a linked list contains a cycle.

    Floyd's Cycle Detection Algorithm (Tortoise and Hare).

    Concept
    -------
    If the linked list has a cycle, the fast pointer will eventually
    meet the slow pointer.

    Visualization
    -------------
    Example cycle:

        1 -> 2 -> 3 -> 4 -> 5
                  ^       |
                  |_______|

    Movement:

        Step 1: slow=2, fast=3
        Step 2: slow=3, fast=5
        Step 3: slow=4, fast=4  (collision)

    Collision indicates the presence of a cycle.

    Parameters
    ----------
    head : ListNode
        Head node of the linked list.

    Returns
    -------
    bool
        True if a cycle exists, otherwise False.

    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(1)
    """

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


def detect_cycle_start(head):
    """
    Find the node where a cycle begins in a linked list.

    Concept
    -------
    Step 1: Detect cycle using slow and fast pointers.

    Step 2: Once they meet:
            - Move one pointer to head
            - Move both pointers one step at a time

    The node where they meet again is the start of the cycle.

    Mathematical Insight
    --------------------
    If:
        L = distance from head to cycle start
        C = cycle length

    When slow and fast meet:
        slow has traveled L + x
        fast has traveled 2(L + x)

    This property allows us to find the exact cycle entry point.

    Parameters
    ----------
    head : ListNode
        Head node of the linked list.

    Returns
    -------
    ListNode or None
        The node where the cycle starts, or None if no cycle exists.

    Time Complexity
    ---------------
    O(n)

    Space Complexity
    ----------------
    O(1)
    """

    slow = head
    fast = head

    # Detect collision
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return None

    slow = head

    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def build_linked_list(values):
    """
    Utility function to build a linked list from a Python list.

    Parameters
    ----------
    values : list
        List of values to convert into a linked list.

    Returns
    -------
    ListNode
        Head node of the linked list.
    """

    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for v in values[1:]:
        current.next = ListNode(v)
        current = current.next

    return head


if __name__ == "__main__":
    """
    Example usage of the slow-fast pointer algorithms.
    """

    head = build_linked_list([1, 2, 3, 4, 5])

    middle = find_middle(head)
    print("Middle node value:", middle.val)

    print("Cycle exists:", has_cycle(head))
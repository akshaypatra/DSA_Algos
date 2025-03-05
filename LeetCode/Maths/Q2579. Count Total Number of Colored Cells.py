'''

2579. Count Total Number of Colored Cells
Solved
Medium

There exists an infinitely large two-dimensional grid of uncolored unit cells. You are given a positive integer n, indicating that you must do the following routine for n minutes:

At the first minute, color any arbitrary unit cell blue.
Every minute thereafter, color blue every uncolored cell that touches a blue cell.
Below is a pictorial representation of the state of the grid after minutes 1, 2, and 3.


Return the number of colored cells at the end of n minutes.

 

Example 1:

Input: n = 1
Output: 1
Explanation: After 1 minute, there is only 1 blue cell, so we return 1.
Example 2:

Input: n = 2
Output: 5
Explanation: After 2 minutes, there are 4 colored cells on the boundary and 1 in the center, so we return 5. 
 

Constraints:

1 <= n <= 105

'''

class Solution:
    def coloredCells(self, n: int) -> int:
        # The formula calculates the number of colored cells in a particular pattern,
        # where n represents the size of the grid.
        # It is based on a mathematical observation that with each increase in n,
        # there are 2*(n-1) additional colored cells from the previous step,
        # plus the center cell which is always colored.

        # Calculate the number of colored cells using the given formula:
        # 2 * n * (n - 1) is the pattern growth as we move to larger grids,
        # +1 accounts for the center cell, which is always colored.
        return 2 * n * (n - 1) + 1
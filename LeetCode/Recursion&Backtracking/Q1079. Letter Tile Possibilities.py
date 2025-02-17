'''

1079. Letter Tile Possibilities
Solved
Medium
Topics
Companies
Hint
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1
 

Constraints:

1 <= tiles.length <= 7
tiles consists of uppercase English letters.

'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def dfs(tile_counter: Counter) -> int:
            combinations_count = 0  # Initialize the count of combinations.
          
            # Iterate through each tile in the counter.
            for tile, count in tile_counter.items():
                # If there is at least one tile available, use one to form a new sequence.
                if count > 0:
                    combinations_count += 1  # Include this tile as a new possibility.
                    tile_counter[tile] -= 1  # Use one tile.
                 
                    # Recursively count further possibilities by using the recently used tile.
                    combinations_count += dfs(tile_counter)
                  
                    # Undo the choice to backtrack and allow for different combinations.
                    tile_counter[tile] += 1
          
            # Return the total number of combinations.
            return combinations_count

        # Count the occurrences of each tile.
        tile_counter = Counter(tiles)
      
        # Start DFS with the count of available tiles to find all possible combinations.
        return dfs(tile_counter)

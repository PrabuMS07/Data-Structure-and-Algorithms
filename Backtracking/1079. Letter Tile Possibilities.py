"""You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

"""

from typing import Counter


class Solution(object):
    def numTilePossibilities(self, tiles):

        count = Counter(tiles)

        def dfs():
            res = 0
            for p in count:
                if count[p] > 0:
                    count[p]-=1
                    res+=1
                    res += dfs()
                    count[p]+=1
            return res
        # dfs()
        return dfs()


obj = Solution()

print(obj.numTilePossibilities(tiles = "AAB"))
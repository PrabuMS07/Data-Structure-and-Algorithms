"""Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

class Solution(object):
    def exist(self, board, word):
        row,col = len(board),len(board[0])

        seen = set()

        def dfs (r,c,i):
            
            if i == len(word):
                return True

            if c >= col or r >= row or c < 0 or r < 0 or (r,c) in seen or board[r][c]!=word[i]:
                return False
            seen.add((r,c))
            res = (dfs(r+1,c,i+1) or dfs(r,c-1,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1))
            seen.remove ((r,c))
            return res
        
        for r in range(row):
            for c in range(col):
                if dfs(r,c,0):
                    return True
        return False

        
obj = Solution()

print(obj.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))
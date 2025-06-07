"""You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.
"""

class Solution(object):
    def minimumRecolors(self, blocks, k):

        
        l = 0
        c = 0 
        m = k
        for i in range (len(blocks)):

            if blocks[i] == "W":
                c+=1

            if i-l+1 == k:
                m = min(m,c)
                if blocks[l] == "W":
                    c-=1
                l+=1
        return m

obj = Solution()

print(obj.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))
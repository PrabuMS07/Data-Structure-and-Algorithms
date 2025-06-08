"""Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in seen and l<r:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            res = max(res,r-l+1)
        return res
        
            
obj = Solution()

print(obj.lengthOfLongestSubstring(s = "abcabcbb"))
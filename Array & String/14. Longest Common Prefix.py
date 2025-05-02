"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"""

class Solution(object):
    def longestCommonPrefix(self, strs):

        l=len(strs[0]) #find smallest value
        for i in strs:
            if l > len(i):
                l = len(i)

        i = 0
        while i < l:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            
            i+=1
        
        return strs[0][:i]

obj = Solution()
print(obj.longestCommonPrefix(strs = ["flower","flow","flight"]))
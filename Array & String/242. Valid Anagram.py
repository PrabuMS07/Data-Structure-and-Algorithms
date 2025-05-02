"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true"""


class Solution(object):
    def isAnagram(self, s, t):

        if len(s)!= len(t):
            return False
        sd,td = {},{}
        for i in range (len(s)):
            if (( 1+sd.get(s[i],0)) !=  (1+td.get(t[i],0))):
                return False
            else:
                sd[s[i]] = 1+sd.get(s[i],0)
                td[t[i]] = 1+td.get(t[i],0)
        return True


obj = Solution()
print(obj.isAnagram(s = "anagram", t = "nagaram"))


        
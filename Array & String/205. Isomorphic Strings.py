"""Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
"""

class Solution(object):
    def isIsomorphic(self, s, t):

        if len (s) != len(t):
            return False
        seen = {}

        for i in range (len(s)):
            if s[i] in seen:
                if seen[s[i]] != t[i]:
                    return False
                continue
            if t[i] in seen.values():
                return False
            seen[s[i]] = t[i]
        return True
            
obj = Solution()

print(obj.isIsomorphic(s = "egg", t = "add"))
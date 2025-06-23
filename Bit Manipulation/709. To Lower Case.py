"""Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

 

Example 1:

Input: s = "Hello"
Output: "hello"

"""

class Solution(object):
    def toLowerCase(self, s):
        res = ""
        for i in range (len(s)):

            if 'A' <= s[i] <= "Z":
                res += chr(ord(s[i]) ^ 32)
            else:
                res += s[i]
        return res
        
obj = Solution()

print(obj.toLowerCase(s = "Hello"))
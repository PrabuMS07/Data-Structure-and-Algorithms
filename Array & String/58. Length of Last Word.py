"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5."""

class Solution(object):
    def lengthOfLastWord(self, s):
        c = 0
        for i in range (len(s)-1,-1,-1):
            if c == 0 and s[i] == " ":
                continue
            if s[i]==" ":
                break
           
            c +=1
        return c

obj = Solution()
print(obj.lengthOfLastWord(s = "Hello World"))
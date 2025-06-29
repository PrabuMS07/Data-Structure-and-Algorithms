"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""

class Solution(object):
    def generateParenthesis(self, n):

        res = []

        def Backtrack (openN , closeN , cur):

            if openN == closeN == n:
                res.append(cur[:])
                return 
            
            if openN < n:
                Backtrack(openN+1,closeN,cur+"(")
            
            if closeN < openN:
                Backtrack(openN,closeN+1,cur+")")

        Backtrack(0,0,"")
        return res

obj = Solution()

print(obj.generateParenthesis(n = 3))
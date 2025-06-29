"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""

class Solution(object):
    def generateParenthesis(self, n):

        res = []
        stack = []

        def Backtrack (openN , closeN):

            if openN == closeN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                Backtrack(openN+1,closeN)
                stack.pop()
            
            if closeN < openN:
                stack.append(")")
                Backtrack(openN,closeN+1)
                stack.pop()

        Backtrack(0,0)
        return res

obj = Solution()

print(obj.generateParenthesis(n = 3))
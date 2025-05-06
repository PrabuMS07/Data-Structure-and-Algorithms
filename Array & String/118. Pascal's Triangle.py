"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"""

class Solution(object):
    def generate(self, numRows):
        result = [[1]]

        for i in range (numRows - 1):

            current = [0] + result[-1]+ [0]
            next = []
           
            for j in range(len(current)-1):
                next.append(current[j]+current[j+1])             
            result.append(next)
        return result

obj = Solution()
print(obj.generate(numRows = 5))
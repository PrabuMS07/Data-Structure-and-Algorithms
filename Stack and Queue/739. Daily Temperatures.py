"""Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
       
        res = [0]*len(temperatures)
        s = []

        for i in range(len(temperatures)):
            cur = temperatures [i]

            while s and s[-1][0] < cur:
                val,index = s.pop()
                res[index] = i - index

            else:
                s.append((cur,i))
        return res

obj = Solution()

print(obj.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
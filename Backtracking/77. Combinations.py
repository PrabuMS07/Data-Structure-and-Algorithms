"""Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []

        def rec (i,cur):
            if len(cur) == k:
                res.append (cur[:])
                return 

            if i > n or len(cur) > k:
                return 

            cur.append(i)
            rec (i+1,cur)
            cur.pop()
            
            rec(i+1,cur)

        rec(1,[])

        return res

obj = Solution()

print(obj.combine(n = 4, k = 2))
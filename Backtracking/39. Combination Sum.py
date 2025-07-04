"""Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []


        def rec (i,cur,total):
            if target == total:
                res.append(cur[:])
                return 

            if i >= len(candidates) or target < total:
                return

            cur.append(candidates[i])
            rec (i,cur,total+candidates[i])

            cur.pop()
            rec (i+1,cur,total)

        rec(0,[],0)
        return res


obj = Solution()

print(obj.combinationSum(candidates = [2,3,6,7], target = 7))
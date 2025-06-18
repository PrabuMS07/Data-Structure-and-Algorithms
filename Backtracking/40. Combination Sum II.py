"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""

class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def rec (i,cur,total):

            if total == target:
                res.append(cur[:])
                return 

            if i >= len(candidates) or target < total:
                return 

            cur.append(candidates[i])
            rec (i+1,cur,total+candidates[i])

            while i+1 < len(candidates) and candidates[i] == candidates[i+1] :
                i+=1

            cur.pop()
            rec (i+1,cur,total)

        rec(0,[],0)
        return res
        
obj = Solution()

print(obj.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
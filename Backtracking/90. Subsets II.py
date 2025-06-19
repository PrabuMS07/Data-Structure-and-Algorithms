"""Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

class Solution(object):
    def subsetsWithDup(self, nums):

        res = []
        nums.sort()
        def rec (i,cur):
            if len(nums) <= i:
                res.append(cur[:])
                return 

            cur.append(nums[i])
            i+=1
            rec(i,cur)
            while i < len(nums) and nums[i] == nums[i-1]:
                i+=1
            cur.pop()
            rec(i,cur)
        rec(0,[])
        return res
        
obj = Solution()

print(obj.subsetsWithDup(nums = [1,2,2]))
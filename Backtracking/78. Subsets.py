"""Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        ls = []
        def rec (i):
            if i >= len(nums):
                res.append(ls[:])
                # print (res)
                return
            ls.append (nums[i])
            rec(i+1)
            ls.pop()
            rec(i+1)


        rec(0)
        return res

obj = Solution()

print(obj.subsets(nums = [1,2,3]))
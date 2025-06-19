"""Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

class Solution(object):
    def permute(self, nums):

        if len(nums) == 0:
            return [[]]

        perm = self.permute(nums[1:])
        res = []

        for p in perm:
            for i in range(len(p)+1):
                p_copy = p[:]
                p_copy.insert (i,nums[0])
                res.append(p_copy[:])

        return res

obj = Solution()

print(obj.permute(nums = [1,2,3]))
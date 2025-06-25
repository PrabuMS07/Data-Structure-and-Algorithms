"""Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
 
 """

from collections import Counter


class Solution(object):
    def permuteUnique(self, nums):
        res = []
        perm = []

        count = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[:])
                return 

            for p in count:
                if count[p] > 0:
                    perm.append(p)
                    count[p]-=1
                    dfs()
                    perm.pop()
                    count[p]+=1
        dfs()
        return res


obj = Solution()

print(obj.permuteUnique(nums = [1,1,2]))
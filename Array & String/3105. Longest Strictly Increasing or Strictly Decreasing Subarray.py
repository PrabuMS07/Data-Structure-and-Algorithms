"""You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

 

Example 1:

Input: nums = [1,4,3,3,2]

Output: 2

Explanation:

The strictly increasing subarrays of nums are [1], [2], [3], [3], [4], and [1,4].

The strictly decreasing subarrays of nums are [1], [2], [3], [3], [4], [3,2], and [4,3].

Hence, we return 2.
"""

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        inc = dec = 1
        res = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                inc = dec = 1
            elif nums[i] > nums[i - 1]:
                inc, dec = inc + 1, 1
            else:
                inc, dec = 1, dec + 1

            res = max(res, inc, dec)

        return res


obj = Solution()

print(obj.longestMonotonicSubarray(nums = [1,4,3,3,2]))
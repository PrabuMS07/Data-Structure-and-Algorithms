"""

Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

"""

class Solution(object):
    def maxAscendingSum(self, nums):

        curr = ans = nums[0]
        for i in range(1, len(nums)):
            curr = curr + nums[i] if nums[i] > nums[i-1] else nums[i]
            ans = max(ans, curr)
        return ans
        
obj = Solution()
print(obj.maxAscendingSum([10,20,30,5,10,50]))
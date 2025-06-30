"""The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.

 

Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

"""

class Solution(object):
    def maxProductDifference(self, nums):

        max1 = max2 = 0
        min1 = min2 = float('inf')

        for i in nums:
            if i > max2:
                if i > max1:
                    max2 = max1
                    max1 = i
                else:
                    max2 = i

            if i < min2:
                if i < min1:
                    min2 = min1
                    min1 = i
                else:
                    min2 = i

        return (max1*max2) - (min1*min2)
    
obj = Solution()

print(obj.maxProductDifference(nums = [5,6,2,7,4]))
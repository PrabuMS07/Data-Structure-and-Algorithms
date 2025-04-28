"""

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

"""


class Solution(object):
    def sortedSquares(self, nums):

        left = 0
        right = len(nums)-1
        result = []
        while left <=right:

            if abs(nums[left]) < abs(nums[right]):
                result.append(nums[right]**2)
                right-=1
            else:
                result.append(nums[left]**2)
                left+=1
        return result[::-1]

obj = Solution()
print(obj.sortedSquares([-4,-1,0,3,10]))
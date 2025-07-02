"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""

class Solution(object):
    def searchRange(self, nums, target):
    
        l = 0
        r = len(nums)-1
        v = -1
        while (l<=r):

            m = (l+r)//2
            if nums[m] == target:
                v = m
                break
            elif nums[m]>target:
                r = m-1
            else:
                l = m+1  
        l = v
        r = v 
        if v != -1:

            while l-1 >=0 and nums[l-1] == nums[l]:
                l-=1
            while r+1 < len(nums) and nums[r+1] == nums[r]:
                r+=1
            return [l,r]
        else:
            return [-1,-1]

obj = Solution()

print(obj.searchRange(nums = [5,7,7,8,8,10], target = 8))
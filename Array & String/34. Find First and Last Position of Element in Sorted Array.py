"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

"""

class Solution(object):
    def searchRange(self, nums, target):
    
        low = 0
        high = len(nums)-1
        index = -1
        while (low<=high):

            mid = (low+high)//2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid]>target:
                high = mid-1
            else:
                low = mid+1  
        left = index
        right = index
        if index != -1:

            while left-1 >=0 and nums[left-1] == nums[left]:
                left-=1
            while high+1 < len(nums) and nums[high+1] == nums[high]:
                high+=1
            return [right,left]
        else:
            return [-1,-1]

obj = Solution()

print(obj.searchRange(nums = [5,7,7,8,8,10], target = 8))
"""Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
"""

# Boyer-Moore Majority Vote Algorithm

class Solution(object):
    def majorityElement(self, nums):
        element, count = None ,0
        for i in range (len(nums)):
            if count == 0:
                count+=1
                element = nums[i]
            elif element == nums[i]:
                count+=1
            else:
                count-=1
        return element 

        
obj = Solution()

print(obj.majorityElement(nums = [3,2,3]))
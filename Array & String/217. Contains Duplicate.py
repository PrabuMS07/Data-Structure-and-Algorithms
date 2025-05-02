"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3."""

class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
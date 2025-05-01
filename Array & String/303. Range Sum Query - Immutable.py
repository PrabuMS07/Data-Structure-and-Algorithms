"""Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3] """


class NumArray(object):

    def __init__(self, nums):
        self.n = nums
        

    def sumRange(self, left, right):
        return sum(self.n[left:right+1])
        s = 0
        while left<=right:
            s += self.n[left]
            left+=1
        return s

        


# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])

param_1 = obj.sumRange(left=0,right=2)
print(param_1)

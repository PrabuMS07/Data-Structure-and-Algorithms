"""Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

"""


class NumArray(object):

    def __init__ (self,nums):
        self.prefix =[0]
        val = 0
        for i in range(len(nums)):
            val += nums[i]
            self.prefix.append(val)
    
    def sumRange(self,left ,right):

        return self.prefix[right+1] - self.prefix[left]
            


# Your NumArray object will be instantiated and called as such:
obj = NumArray(nums=[-2, 0, 3, -5, 2, -1])

Q1= obj.sumRange(left=0,right=2)

print(Q1)

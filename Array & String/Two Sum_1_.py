class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for i , val in enumerate(nums):
            n = target - val 
            # print(seen)
            if n in seen :
                return seen[n],i
            seen [val] = i 
        return None
    
obj = Solution()

nums = [2,7,11,15]
target = 9
print(obj.twoSum(nums,target))
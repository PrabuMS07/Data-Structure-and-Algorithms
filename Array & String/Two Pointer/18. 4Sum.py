"""Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]"""


class Solution(object):
    def fourSum(self, nums, target):
        

        res = []

        nums.sort()

        for i in range(len(nums)-1):

            if i>0 and nums[i] == nums[i-1]:
                continue 

            for j in range(i+1,len(nums)-1):

                if j>i+1 and nums[j] == nums[j-1]:
                    continue

                l , r = j+1,len(nums)-1

                while l<r:

                    t = nums[i]+nums[j]+nums[l]+nums[r]

                    if t > target:
                        r-=1
                    elif t<target:
                        l+=1
                    else:
                        res.append([nums[i],nums[j],nums[l],nums[r]])
                        l+=1
                        r-=1
                        while nums[l] == nums[l-1] and l<r:
                            l+=1
                        while nums[r] == nums[r+1] and r>l:
                            r-=1
        return res
    
obj = Solution()
print(obj.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
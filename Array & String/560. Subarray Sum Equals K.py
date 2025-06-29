"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
"""

class Solution(object):
    def subarraySum(self, nums, k):

        hashmap = {0:1}
        count = 0
        cur = 0

        for i in nums:

            cur += i

            if cur - k in hashmap:
                count += hashmap[cur-k] 
            
            if cur in hashmap:
                hashmap[cur] += 1
            else:
                hashmap[cur] = 1
        return count
                


obj = Solution()

print(obj.subarraySum(nums = [1,1,1], k = 2))
"""The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

 

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):

        nums1Idx = {num : i for i, num in enumerate(nums1)}

        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):

            cur = nums2[i]

            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)
                
        return res

obj = Solution()

print(obj.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
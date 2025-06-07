"""Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
"""
class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):

        l = 0
        count = 0
        sum = 0
        for r in range(len(arr)):
            sum += arr[r]

            if r-l+1 == k:
                avg = sum//k

                if avg >= threshold:
                    count+=1

                sum -= arr[l]
                l+=1
        return count
obj = Solution()

print(obj.numOfSubarrays(arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4))
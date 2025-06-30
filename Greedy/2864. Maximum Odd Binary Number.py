"""You are given a binary string s that contains at least one '1'.

You have to rearrange the bits in such a way that the resulting binary number is the maximum odd binary number that can be created from this combination.

Return a string representing the maximum odd binary number that can be created from the given combination.

Note that the resulting string can have leading zeros.

 

Example 1:

Input: s = "010"
Output: "001"
Explanation: Because there is just one '1', it must be in the last position. So the answer is "001".

"""

class Solution(object):
    def maximumOddBinaryNumber(self, s):
        res = ""
        count=0
        for i in s:
            if i == "1":
                count += 1
        return (count-1)*"1" + (len(s)-count)*"0" + "1"

            
obj = Solution()

print(obj.maximumOddBinaryNumber(s = "010"))
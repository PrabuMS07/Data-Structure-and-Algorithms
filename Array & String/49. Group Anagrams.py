"""Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other."""
from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):

        ans = defaultdict(list)

        for i in strs:
            al = [0]*26
            for j in i:

                al [ord(j) - ord("a")] +=1
            
            al = tuple(al)

            ans[al].append(i)
            # print(ans)
        return ans.values()

obj = Solution()
print(obj.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
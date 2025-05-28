"""You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present at the indices ranging from li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].
"""
class Solution(object):
    def vowelStrings(self, words, queries):
        vowel_set = set("aeiou")
        count = [0]
        res = []

        for i in words:
            if i[0] in vowel_set and i[-1] in vowel_set:
                count.append(count[-1]+1)
                continue 
            count.append(count[-1])
        
        for left,right in queries:
            res.append(count[right+1] - count[left])

        return res


obj = Solution()
print(obj.vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]))
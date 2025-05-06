"""Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

 

Example 1:

Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer."""

class Solution(object):
    def stringMatching(self, words):

        res = []

        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue

                if words[i] in words[j]:
                    res.append(words[i])
                    break

        return res
        

obj = Solution()
print(obj.stringMatching(words = ["mass","as","hero","superhero"]))
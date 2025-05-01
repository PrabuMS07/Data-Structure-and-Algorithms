"""Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm"."""

class Solution(object):
    def reverseVowels(self, s):
        v = set(["a","e","i","o","u","A","E","I","O","U"])
        str1 = list (s)
        i = 0
        j = len(s)-1

        while i<j:
            if str1[i] not in v:
                i+=1
            elif str1[j] not in v:
                j-=1
            else:
                str1[i],str1[j] = str1[j],str1[i]
                i+=1
                j-=1        
        return ''.join(str1)

obj = Solution()
print(obj.reverseVowels("IceCreAm"))
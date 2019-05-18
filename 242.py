'''
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        flag = False
        if sorted(s) == sorted(t):
            flag = True
        return flag
        '''
        if collections.Counter(s) == collections.Counter(t):
            return True
        return False

test = Solution()
ind0 = test.isAnagram("anagram","nagaram")
print(ind0)

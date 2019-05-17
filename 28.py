'''
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        lenofneedle = len(needle)
        if lenofneedle == 0:
            return 0
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+lenofneedle] == needle:
                    return i
            return -1
        '''
        if haystack == "" or needle == "" :
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                for j in range(len(needle)):
                    if haystack[i+j] != needle[j]:
                        break
                else:
                    return i
            return -1
        '''
test = Solution()
ind0 = test.strStr("hello","ll")
print(ind0)

ind1 = test.strStr("aaaaa","bba")
print(ind1)

ind2 = test.strStr("","")
print(ind2)

ind3 = test.strStr("mississippi","issip")
print(ind3)

import pdb

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        le = len(s)
        print(le)

        if le == 0 or le == 1:
            return s
        else:
            sub = s[0:1]
            for i in range(le-1):
                def is_Palindrome(s, l, r):
                    while l>=0 and r<le and s[l]==s[r]:
                        l-=1
                        r+=1
                    return s[l+1:r]
                s1 = is_Palindrome(s, i, i)
                if len(s1)>len(sub):
                    sub = s1
                s2 = is_Palindrome(s, i, i+1)
                if len(s2)>len(sub):
                    sub=s2
            return sub

A = Solution()
s = 'xaabaab'

longestPalindrome = A.longestPalindrome(s)
print('The longest Palindrome string is: ', longestPalindrome)
'''
151. Reverse Words in a String
Given an input string, reverse the string word by word.

Example 1:
Input: "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
'''
class Solution:
    def reverseWords(self, s):
        s_new = s.strip()
        strlist = s_new.split()
        reverselist = []
        l = len(strlist) - 1

        for i in range(l, -1, -1):
            reverselist.append(strlist[i])

        reversestr = " ".join(reverselist)
        return reversestr

test = Solution()
ind0 = test.reverseWords("a good   example")
print(ind0)
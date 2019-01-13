import re

class Solution:
    def longestCommonPrefix(self, strs):
        l = len(strs)
        prefix = strs[0]
        i = 1
        for i in range(l):
            match = re.match(prefix, strs[i])
            while not match:
                prefix = prefix[:-1]
                match = re.match(prefix, strs[i])
            print(prefix)
        print(prefix)
        return prefix
        """
        ===========
        solution 1:
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                print(strs[0][:i])
                return strs[0][:i]
        else:
            print(min(strs))
            return min(strs)
        ===========
        solution 2:
        if not strs:
            return ''
        prefix = strs[0]
        for i in range(1, len(strs)):
            match = re.match(prefix, strs[i])
            while not match:
                prefix = prefix[:-1]
                match = re.match(prefix, strs[i])
        return prefix
        """

A = Solution()
#A.longestCommonPrefix(["slower","slow","sloig","sto"])
A.longestCommonPrefix(["flower","flight","flow"])

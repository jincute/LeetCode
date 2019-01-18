import pdb

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        lis = list(s)
        lis_temp = []
        longest_lis = []
        l = len(lis)
        i = j = len_lis =0
        ll = len(longest_lis)
        is_Palindrome = False
        if l <= 1:
            longest_str = "".join(lis)
        elif l == 2:
            if lis[0] == lis[1]:
                longest_str = "".join(lis)
            else:
                longest_str = "".join(lis[0])
        else:
            while i < l:
                j = i + 1
                while j < l:
                    if lis[j] == lis[i]:
                        lis_temp = lis[i:j+1]
                        len_lis = len(lis_temp)

                        min_len = len_lis%2

                        if min_len == 0:
                            if lis_temp[0:int(len_lis/2)] == lis_temp[len_lis:int(len_lis/2-1):-1]:
                                is_Palindrome = True

                        else:
                            if lis_temp[0:int(len_lis/2)] == lis_temp[int(len_lis):int(len_lis/2):-1]:
                                is_Palindrome = True

                        if is_Palindrome == True:

                            print('lis_temp:', lis_temp)
                            print('min_len:', min_len)
                            #pdb.set_trace()

                            if ll < len_lis:
                                longest_lis = lis_temp
                                ll = len_lis

                        else:
                            if ll == 0:
                                longest_lis = lis_temp[0]

                    is_Palindrome = False
                    j = j + 1
                i = i + 1
                longest_str = "".join(longest_lis)
        return longest_str


A = Solution()
s = 'aaabaaaa'   # return "aaabaaa"
#s = 'bb'
longestPalindrome = A.longestPalindrome(s)
print('The longest Palindrome string is: ', longestPalindrome)
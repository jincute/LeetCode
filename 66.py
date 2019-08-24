import pdb

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        num = 0
        for i in range(n):
            num = num + digits[i]*10**(n-1-i)
        new_num = num+1
        # transfer int to list
        new_digits = [int(x) for x in str(new_num)]
        return new_digits
        
        
A = Solution()
le = A.plusOne([9,9])
#le = A.plusOne([1,2,9])
print(le)
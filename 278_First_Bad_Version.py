# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        Time Limit Exceeded
        '''
        # if n < 2:
        #     return 1
        # mid = n//2
        # while 1<=mid<=n:
        #     if isBadVersion(mid) == False:
        #         while mid < n:
        #             if isBadVersion(mid+1) == True:
        #                 return mid+1
        #             mid += 1
        #     else:
        #         if isBadVersion(mid-1) == False:
        #             return mid
        #         else:
        #             mid = mid // 2

        '''
        Time Limit Exceeded
        '''
        # if n < 2:
        #     return 1
        # mid = n//2
        # while 1 <= mid <= n:
        #     if isBadVersion(mid) == isBadVersion(mid+1) == False:
        #         mid = (mid+1+n)//2
        #     elif isBadVersion(mid) == isBadVersion(mid+1) == True:
        #         mid = (1+mid)//2
        #     else:
        #         return mid

        '''
        二分法适用范围：单调性问题一定可以用二分法解，但用二分法解的不一定是单调性问题
        寻找左右边界；初始边界 left=1, right=n。每次检测 mid=(left+right)//2
        判断 isBadVersion(mid):
        True: 更新 right = mid
        False: 更新 left = mid + 1
        终止条件：right-left <= 1 (相邻或者重合)
        '''

        left = 1
        right = n
        while right - left > 1:
            mid = (left + right) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            elif isBadVersion(mid) == True:
                right = mid

        if isBadVersion(left):
            return left
        else:
            return right


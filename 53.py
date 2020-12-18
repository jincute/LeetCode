"""
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Solution1: DP
        state transition: f[i] = f[i-1] ? nums[i]+f[i-1]:nums[i]
        '''
        l = len(nums)
        # li = [0]
        value = 0
        max_value = nums[0]
        for i in range(l):
            value = max(value+nums[i],nums[i])
            if value > max_value:
                max_value = value
            # li.append(maxnum(li[i]+nums[i],nums[i]))
            # print('li: ', li)
        #print(max(li))
        # return max(li[1:])
        return max_value

    '''
    Solution1: Divide and Conquer
    经典算法：快速排序，归并排序
    实现方式：循环递归。分解若干个子问题，子问题逐步解决。
    '''

    def maxSubArray2(self, nums):
        return self.divide_and_conquer(nums, 0, len(nums)-1)

    def divide_and_conquer(self, nums, low, high):
        # boundary
        if low == high:
            return nums[low]

        mid = (low+high)//2
        max_sum_left = self.divide_and_conquer(nums, low, mid)
        max_sum_right = self.divide_and_conquer(nums, mid+1, high)
        cross_suffix = 0
        sum = 0
        for i in range(mid-1, low-1, -1):
            sum += nums[i]
            cross_suffix = max(sum, cross_suffix)
        cross_prefix = 0
        sum = 0
        for j in range(mid+1,high+1):
            sum += nums[j]
            cross_prefix = max(sum, cross_prefix)

        cross_sum_max = cross_prefix + cross_suffix + nums[mid]
        return max(max_sum_left, max_sum_right, cross_sum_max)


A = Solution()
r = A.maxSubArray2([1,2,-2,4,-1,1,2,-5,2])
print(r)

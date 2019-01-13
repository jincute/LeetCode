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
        def maxnum(n1, n2):
            if n1>=n2:
                return n1
            else:
                return n2

        value = nums.split(',')
        #print(value)
        l = len(value)
        li = []
        li.append(0)
        for i in range(0, l):
            li.append(maxnum(li[i]+int(value[i]),int(value[i])))
        #print(max(li))
        return max(li[1:])
'''
        li = []
        li[0] = 0
        for i in range(0, l):
            li.append(max(li[i]+int(value[i]),int(value[i])))
        print(li)
'''



A = Solution()
A.maxSubArray("-2,1,-3,4,-1,2,1,-5,4")

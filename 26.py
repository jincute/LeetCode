"""
26. Remove Duplicates from Sorted Array
test case: [1,1,2]
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = nums.split(',')
        l = len(nums)
        l1 = 1
        if l < 2:
            return l
        else:
            for i in range(1, l):


        print(l)

A = Solution()
A.removeDuplicates("0,0,1,1,1,2,2,3,3,4")

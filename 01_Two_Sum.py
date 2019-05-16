class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        """
        n = len(nums)
        hasharr = {}
        for i in range(n):
            j = target - nums[i]
            if j in hasharr:
                return hasharr[j],i
            else:
                hasharr[nums[i]] = i

A = Solution()
a, b = A.twoSum([2,7,11,17], 9)
print(a,b)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        init = 0
        for n in nums:
            if n == init:
                init += 1
            else:
                return init
        return len(nums)
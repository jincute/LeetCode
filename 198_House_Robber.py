class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)
        else:
            dp = [i for i in range(n)]
            dp[0] = nums[0]
            dp[1] = nums[1]
            dp[2] = nums[0] + nums[2]
            for i in range(3,n):
                dp[i] = max(dp[i-2]+nums[i],dp[i-3]+nums[i])
        return max(dp[-1],dp[-2])
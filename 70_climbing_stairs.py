class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [x for x in range(n+1)]
        if n == 1:
            dp[1] = 1
        elif n == 2:
            dp[2] = 2
        else:
            for i in range(3, n+1):
                dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

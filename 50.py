class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        291 / 304 pass, time limit exceeded
        '''
        result = 1
        if x <
        for i in range(abs(n)):
            result *= x
        if n < 0:
            result = 1/result
        return round(result,5)

S = Solution().myPow(0.00001, 2147483647)
print(S)

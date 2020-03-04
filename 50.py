class Solution:
    def myPow(self, x: float, n: int) -> float:
        '''
        291 / 304 pass, time limit exceeded
        '''
        '''
        result = 1
        for i in range(abs(n)):
            result *= x
        if n < 0:
            result = 1/result
        return round(result,5)
        '''
        if n == 0:
            return 1
        if n < 0 :
            return 1/self.myPow(x,-n)
        if n%2 ==1:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)

S = Solution().myPow(0.00011, 21254)
print(S)

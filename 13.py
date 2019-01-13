class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        num = []
        def assignValue(f):
            if f == 'M':
                return 1000
            elif f == 'D':
                return 500
            elif f == 'C':
                return 100
            elif f == 'L':
                return 50
            elif f == 'X':
                return 10
            elif f == 'V':
                return 5
            elif f == 'I':
                return 1

        roman = list(s)
        l = len(roman)
        #print(roman)
        for i in range(l):
            num.append(assignValue(roman[i]))
            #print(num[i])
        for i in range(l-1):
            if num[i]<num[i+1]:
                sum = sum - num[i]
            else:
                sum = sum + num[i]
        sum = sum + num[l-1]
        print(sum)
        return sum


A = Solution()
#A.romanToInt('MCMXCIV')
A.romanToInt('III')

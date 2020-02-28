import re
import pdb
class Solution:
    def myAtoi(self, str: str) -> int:
        '''
        # Solution 1

        str = str.strip()
        str = str.split()
        final = 0

        if str:
            result = re.findall('(^[\+\-0]*\d*)\D*', str[0])

            MAX_INT = 2147483647
            MIN_INT = -2147483648

            if result:
                try:
                    final = int(''.join(result))
                    if  final > MAX_INT:
                        final = MAX_INT
                    elif final < MIN_INT:
                        final = MIN_INT
                except:
                    final = 0
        return final
        '''
        str = str.strip()
        str = str.split()
        final = 0
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31


S = Solution().myAtoi("a")
print(S)

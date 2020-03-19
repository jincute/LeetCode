import pdb
import numpy as np
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ''' 
        solution 1
        '''
        '''
        dj = [[1 for i in range(m)] for j in range(n)]
        for p in range(1, n):
            for q in range(1, m):
                dj[p][q] = dj[p][q-1] + dj[p-1][q]
        return dj[n-1][m-1]
        '''

        '''
        solution2
        '''
        
        dj = np.ones((m,n))
    
        for i in range(1, m):
            dj[i][0] = 1
            for j in range(1, n):
                dj[0][j] = 1
                dj[i][j] = dj[i][j-1] + dj[i-1][j]
        return int(dj[m-1][n-1])
        
m = 7
n = 3
print(Solution().uniquePaths(m, n))
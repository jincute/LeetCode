import pdb
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
    '''
    Time Limit Exceeded
    '''
        '''
        R = []
        length_list = len(nums)
        for i in range(length_list-2):  #-1,0,1,2
            # i=0, p=1,2,3,4, q=2,3,4,5
            #print('i: ', i)
            j = i
            while j < length_list-2:
                j = j+1
                #print('j: ', j)
                sum = nums[i] + nums[j]
                for k in range(j+1, length_list):
                    if -sum == nums[k]:
                        if not sorted([nums[i], nums[j], nums[k]]) in R:
                            R.append(sorted([nums[i], nums[j], nums[k]]))
        return R
        '''
    
S = Solution().threeSum([-1, 0, 1, 2, -1, -4])
#S = Solution().threeSum([1,-1,-1,0])
print(S)

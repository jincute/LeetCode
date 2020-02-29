import pdb
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # passes 311/313, Time limit exceeded
        '''
        R = []
        length_list = len(nums)
        for i in range(length_list-2):  #-1,0,1,2
            # i=0, p=1,2,3,4, q=2,3,4,5
            #print('i: ', i)
            j = i
            while j < length_list-2:
                j = j+1
                sum = nums[i] + nums[j]
                for k in range(j+1, length_list):
                    if -sum == nums[k]:
                        if not sorted([nums[i], nums[j], nums[k]]) in R:
                            R.append(sorted([nums[i], nums[j], nums[k]]))
        return R
        '''
        if len(nums) < 3:
            return []
        R = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    R.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return R

#S = Solution().threeSum([2,7,11])
S = Solution().threeSum([-1,0,1,2,-1,-4])
print(S)

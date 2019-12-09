import pdb
from collections import Counter
class Solution(object):
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        ###
        # Regular solution
        ###
        '''
        l = len(nums)
        new_list = []
        count = 1
        before = None
        if l == 0:
            return 0
        else:
            for num in nums:
                if before != num:
                    before = num
                    new_list.append(num)
                    count = 1
                elif count < 2:
                    new_list.append(num)
                    count += 1
            p = 0
            for number in new_list:
                nums[p] = number
                p += 1
            return p
        '''

        if not nums:
            return 0
        cnt = dict(Counter(nums))
        print(cnt)
        visited = sorted(cnt.keys())
        print(visited)
        pdb.set_trace()
        j = 0
        for num in visited:
            for i in range(min(2, cnt[num])):
                num[j] = num
                j += 1
        return j


A = Solution()
a = A.removeDuplicates([1,1,1,2,3,5,5])
print(a)

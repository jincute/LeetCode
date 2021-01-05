class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n / 2
        # print(mid)
        flag = 1
        for a in range(0, n - 1):
            if nums[a] == nums[a + 1]:
                flag += 1
                if flag - mid > 0:
                    return nums[a]
            else:
                flag = 1

        '''
        divide and conquer
        '''
        # if len(nums) == 1:
        #     return nums[0]
        # mid = len(nums) // 2
        # L = self.majorityElement(nums[:mid])
        # R = self.majorityElement(nums[mid:])
        # if L == R:
        #     return L
        # else:
        #     countl = countr = 0
        #     for i in range(len(nums)):
        #         if L == nums[i]:
        #             countl += 1
        #         elif R == nums[i]:
        #             countr += 1
        #     if countl > countr:
        #         return L
        #     else:
        #         return R
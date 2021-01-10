class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        [0,0,1] wrong answer
        '''
        #         for i in range(len(nums)):
        #             if nums[i] == 0:
        #                 nums[::] = nums[0:i] + nums[i+1:] + [0]
        # #                 print(nums)
        #         return nums

        index = step = 0
        n = len(nums)
        while step < n:
            if nums[step] != 0:
                nums[index] = nums[step]
                index += 1
            step += 1
        for i in range(index, n):
            nums[i] = 0
        return nums

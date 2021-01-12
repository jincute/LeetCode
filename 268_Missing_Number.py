class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        solution 1

        nums.sort()
        init = 0
        for n in nums:
            if n == init:
                init += 1
            else:
                return init
        return len(nums)
        '''

        '''
        solution 2
        数学方法: 求 0 ~ n+1 的值，减去nums的和
        '''

        nums_sum = 0
        total_sum = 0
        for n in nums:
            nums_sum += n
        for i in range(len(nums) + 1):
            total_sum += i
        return total_sum - nums_sum
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n/2
        # print(mid)
        flag = 1
        for a in range(0, n-1):
            if nums[a] == nums[a+1]:
                flag += 1
                if flag - mid > 0:
                    return nums[a]
            else:
                flag = 1
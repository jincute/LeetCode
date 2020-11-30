class Solution:
    def removeDuplicates(nums):
        length = len(nums)
        if nums == None:
            return 0
        if length == 1:
            return 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[temp] = nums[i]
                temp += 1
        return temp


l = [0,0,1,1,1,2,2,3,3,4]
r = Solution.removeDuplicates(l)
print(r)

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2]
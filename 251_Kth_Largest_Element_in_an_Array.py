class Solution:
    def mergeSort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            L = nums[:mid]
            R = nums[mid:]
            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = R[j]
                    j += 1
                k += 1
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                nums[k] = R[j]
                j += 1
                k += 1
        return nums

    def findKthLargest(self, nums: List[int], k: int) -> int:
        #         return sorted(nums)[-k]
        sort_nums = self.mergeSort(nums)
        # print(sort_nums)
        return sort_nums[-k]        
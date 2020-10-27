class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # nk = k%len(nums)
        # pre_nums = nums[-nk:]
        # suffix_nums = nums[0:len(nums)-nk]
        # n_nums = pre_nums + suffix_nums
        # for i in range(len(nums)):
        #     nums[i] = n_nums[i]
        def reverse(li,s,e):
            while s<e:
                tmp = li[s]
                li[s] = li[e]
                li[e] = tmp

                s+=1
                e-=1
            return li

        nk = k%len(nums)
        nums = reverse(nums, 0, len(nums)-1)
        nums = reverse(nums, 0, nk-1)
        nums = reverse(nums, nk, len(nums)-1)


        

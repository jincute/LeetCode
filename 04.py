import pdb
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums = []
        i = j = 0
        if nums1 == [] and nums2 == []:
            nums = []
        elif nums1 == [] and nums2 != []:
            nums = nums2
        elif nums2 == [] and nums1 != []:
            nums = nums1
        else:
            while i < m and j < n:
                if nums2[j] <= nums1[i]:
                    nums.append(nums2[j])
                    j = j+1
                else:
                    nums.append(nums1[i])
                    i = i+1
            #print('i = ', i)
            #print('j = ', j)
            #print('m: ', m)
            #print('n: ', n)
            #pdb.set_trace()
            if i == m:
                for j in range(j, n):
                    nums.append(nums2[j])
            elif j == n:
                for i in range(i, m):
                    nums.append(nums1[i])

        #print(nums)
        l = len(nums)
        if l == 0:
            median = 0
        elif l % 2 == 0:
            median = (nums[int(l/2-1)] + nums[int((l/2-1)+1)])/2
        elif l% 2 !=0:
            median = nums[int((l+1)/2-1)]
        return median

nums1 = [1,2,4,6]
nums2 = [3,4,7,8]

A = Solution()
median = A.findMedianSortedArrays(nums1, nums2)
print(median)


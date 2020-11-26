class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_nums = []
        n1 = len(nums1)
        n2 = len(nums2)
        i,j = 0,0
        sort_nums1 = sorted(nums1)
        sort_nums2 = sorted(nums2)
        while i<n1 and j<n2:
            if sort_nums1[i] < sort_nums2[j]:
                i += 1
            elif sort_nums1[i] > sort_nums2[j]:
                j += 1
            else:
                intersect_nums.append(sort_nums1[i])
                i += 1
                j += 1
        return intersect_nums
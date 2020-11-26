class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersect_nums = []
        set1 = set(nums1)
        set2 = set(nums2)
        for x in set1:
            if x in set2:
                intersect_nums.append(x)
        return intersect_nums
            
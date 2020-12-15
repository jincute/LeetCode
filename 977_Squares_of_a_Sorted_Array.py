class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_list = []
        for n in nums:
            new_list.append(n**2)
        new_list = sorted(new_list)
        return new_list
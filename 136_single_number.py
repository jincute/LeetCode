class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # solution 1: hash table 
        # Time complexity: O(n)
        # Space complexity: O(n)
        n = len(nums)
        if n == 1:
            return nums[0]
        # hash table
        hashtable_length = int(n/2)+1
        li = []
        for i in nums:
    #         print(i)
            if i not in li:
                li.append(i)
            else:
                li.pop(li.index(i))
        return li[0]

        # solution 2: 
        # math: 2∗(a+b+c)−(a+a+b+b+c)=c
        # Time complexity: O(n)
        # Space complexity: O(n)
        nums_unit = []
        pre_total = 0
        total = 0
        for n in nums:
            total += n
            if n not in nums_unit:
                nums_unit.append(n)
                pre_total += 2*n
        return(pre_total - total)

        # solution 3:
        # XOR
        # Time complexity: O(n)
        # Space complexity: O(1)
        a = 0
        for n in nums:
            a = a^n
        return(a)
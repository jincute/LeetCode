import pdb 

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        """
        # brute-force: method
        n = len(height)
        max_area = 0
        smaller = 0
        if n == 1 or n == 0:
            return 0
        else:
            for i in range(n):
                for j in range(n):
                    if j != i:
                        if height[j] > height[i]:
                            smaller = height[i]
                        else:
                            smaller = height[j]
                        area = smaller * abs(j-i)
                        if area > max_area:
                            max_area = area  
            return max_area
        """

        # https://leetcode.wang/leetCode-11-Container-With-Most-Water.html
        n = len(height)
        if n <= 1:
            return 0
        else:
            head = 0
            tail = n-1
            maxArea = min(height[head], height[tail])*(tail-head)
            while(tail-head>1):
                if height[head] <= height[tail]:
                    head += 1
                else:
                    tail -= 1
                auxArea = min(height[head], height[tail])*(tail-head)
                if auxArea > maxArea:
                    maxArea = auxArea
            return maxArea

A = Solution()
le = A.maxArea([1,8,6,2,5,4,8,3,7])
#le = A.maxArea([1,2,1])
print(le)
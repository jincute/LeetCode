import pdb
class Solution:
    def maxProfit(prices):
        length_of_list = len(prices)
        max_profix = [0]
        if length_of_list == 0 or length_of_list == 1:
            return 0
        for i in range(1, length_of_list):
            # print('curr prices list: ', prices[:i])
            min_price = min(prices[:i])
            # print(min_price)
            max_profix.append(max(max_profix[i-1], prices[i]-min_price))
            # print('max_profix: ', max_profix)
        return max_profix[-1]

l = [7]
r = Solution.maxProfit(l)
print(r)
# DP solution

# test cases 1:
# Input: [7,1,5,3,6,4]
# Output: 5

# test case 2:
# Input: [7,6,4,3,1]
# Output: 0

# 经典的一维动态规划
# brute force: O(n^2)
# 观测最大收益 max_profix = max{prices[j] - prices[i]}, 0<=i<j<=n-1
# 而买入: prices[i]: min{prices[k]}, k<=i
# 卖出: prices[j]: max{prices[k]}, k>=j

# track the min price, L[i] - lowest price up to i-th day
# M[i]: max profix up to i-th day
# M[i] = max(M[i-1], prices[i]-L[i]) ***规划方程
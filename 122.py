from typing import List 
import pdb 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices) #days = 6
        profit = 0
        for i in range(1, days):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
            #print('profit: ', profit)
            #pdb.set_trace()
        return profit
        
# 122. Best Time to Buy and Sell Stock II

#stock = [7,1,5,3,6,4]
#stock = [1,2,3,4,5]
stock = [7,6,4,3,1]
print(Solution().maxProfit(stock))

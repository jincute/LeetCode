class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        solution 1
        '''
        # firstBuy, firstSell = float('-inf'), 0
        # secondBuy, secondSell = float('-inf'), 0
        # for price in prices:
        #     firstBuy = max(firstBuy, -price)
        #     firstSell = max(firstSell, firstBuy + price)
        #     secondBuy = max(secondBuy, firstSell - price)
        #     secondSell = max(secondSell, secondBuy + price)
        # return secondSell


        '''
        solution 2
        '''

        if prices == []:
            return 0
        n = len(prices)

        # 结束时的最高利润=[天数][是否持有股票][卖出次数]
        dp = [[[0, 0, 0], [0, 0, 0]] for i in range(0, n)]

        # print(dp)

        # 第一天休息
        dp[0][0][0] = 0

        # 第一天买入
        dp[0][1][0] = -prices[0]

        # 第一天不可能已经有卖出
        dp[0][0][1] = float('-inf')
        dp[0][0][2] = float('-inf')
        dp[0][1][1] = float('-inf')
        dp[0][1][2] = float('-inf')

        for i in range(1, n):
            # 未持股，未卖出过，说明从未进行过买卖
            dp[i][0][0] = 0
            # 未持股，卖出过1次，可能是今天卖的，也可能是之前卖出
            dp[i][0][1] = max(dp[i - 1][1][0] + prices[i], dp[i - 1][0][1])

            # 没有持股，卖出过两次：可能是今天卖出，也可能是之前卖出
            dp[i][0][2] = max(dp[i - 1][1][1] + prices[i], dp[i - 1][0][2])

            # 持股，没有卖出过股票：可能今天买，也可能是之前买
            dp[i][1][0] = max(dp[i - 1][0][0] - prices[i], dp[i - 1][1][0])

            # 持股，卖出过一次股票：可能是今天买，也可能是之前买
            dp[i][1][1] = max(dp[i - 1][0][1] - prices[i], dp[i - 1][1][1])

            # 持股，卖出过两次股票。最多交易2次。所以不存在
            dp[i][1][2] = float('-inf')


            #         print(dp)
        return max(dp[n - 1][0][1], dp[n - 1][0][2], 0)
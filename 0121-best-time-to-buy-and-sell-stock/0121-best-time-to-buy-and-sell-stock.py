class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            profit = prices[i] - buy

            if profit > ans:
                ans = profit

            if prices[i] < buy:
                buy = prices[i]

        return ans
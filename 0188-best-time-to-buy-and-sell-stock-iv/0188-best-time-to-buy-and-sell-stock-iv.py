class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        if n == 0 or k == 0:
            return 0

        # If k is large, it becomes unlimited transactions
        if k >= n // 2:
            profit = 0

            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]

            return profit

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            best = -prices[0]

            for d in range(1, n):
                dp[t][d] = max(
                    dp[t][d - 1],
                    prices[d] + best
                )

                best = max(
                    best,
                    dp[t - 1][d] - prices[d]
                )

        return dp[k][n - 1]
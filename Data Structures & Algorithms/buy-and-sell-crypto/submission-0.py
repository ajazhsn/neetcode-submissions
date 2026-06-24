class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        for i in range(1, len(prices)):
            for j in range(i):
                if prices[i]-prices[j] > 0:
                    max_price = max(max_price,prices[i]-prices[j])

        return max_price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrices = [0] * len(prices)
        maxPrices[-1] = prices[-1]

        for i in range(len(maxPrices)-2, -1, -1):
            if prices[i+1] >= maxPrices[i+1]:
                maxPrices[i] = prices[i+1]
            else:
                maxPrices[i] = maxPrices[i+1]

        res = 0

        for i in range(0,len(prices)):
            if maxPrices[i] - prices[i] > res:
                res = maxPrices[i] - prices[i]

        return res
    
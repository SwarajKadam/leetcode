class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        for i in range (len(prices)-1):
            if prices[i]< prices[i+1]:
                buy = prices[i]
            else:
                continue

            highest = prices[i+1]
            diff = highest - buy

            profit+=diff

        return profit
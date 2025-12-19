class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxprofit = 0

        for i in range(1,len(prices)):
            profit = prices[i]-prices[i-1]
            if profit>0:
                maxprofit +=profit
            else:
                profit =0
        return maxprofit
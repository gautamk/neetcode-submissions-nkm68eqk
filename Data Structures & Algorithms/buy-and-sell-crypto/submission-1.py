class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        li = 0
        ri = 1
        maxProfit = 0
        while ri < len(prices):
            profit = prices[ri] - prices[li]
            if profit > maxProfit:
                maxProfit = profit 
            elif prices[ri] < prices[li]:
                li = ri
            ri+=1
        return maxProfit
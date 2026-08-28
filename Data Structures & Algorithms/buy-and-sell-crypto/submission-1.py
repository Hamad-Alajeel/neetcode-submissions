class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        mp = 0
        days = len(prices)
        while r < days:
            if prices[r]>prices[l]:
                cur_profit = prices[r]-prices[l]
                mp = max(mp,cur_profit)
            else:
                l = r
            r += 1
        return mp
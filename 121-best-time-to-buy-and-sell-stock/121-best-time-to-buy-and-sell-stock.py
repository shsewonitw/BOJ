class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = 100000
        profit = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
                continue
            else:
                profit = price - minPrice if profit < price - minPrice else profit
        
        return profit
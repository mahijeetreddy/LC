class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        mp = 0

        for price in prices:
            if price< min_price:
                min_price = price
            else:
                mp = max(mp, price- min_price)
        return mp

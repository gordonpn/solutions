class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = float('-inf')
        buy_price = float('inf')
        
        for price in prices:
            buy_price = min(buy_price, price)
            
            if price - buy_price > profit:
                profit = price - buy_price
        
        return profit 
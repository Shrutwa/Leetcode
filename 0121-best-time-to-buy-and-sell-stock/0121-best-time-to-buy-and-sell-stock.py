class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_pointer = 0
        sell_pointer = 1
        max_profit = 0
        
        while sell_pointer < len(prices):
            currentProfit = prices[sell_pointer] - prices[buy_pointer] 
            if prices[buy_pointer] < prices[sell_pointer]:
                max_profit =max(currentProfit,max_profit)
            else:
                buy_pointer = sell_pointer
            sell_pointer += 1
        return max_profit
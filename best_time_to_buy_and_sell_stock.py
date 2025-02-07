from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) ->int:
        buy = 0
        sell = 1
        maxProfit =0
        while sell < len(prices):
            # if sell price > buy price, try the next sell
            if prices[sell] > prices[buy]:
                maxProfit = max(maxProfit,prices[sell] - prices[buy])
                sell += 1
            # if sell price < buy price, set the buy to sell
            else:
                buy = sell
                sell +=1
        return maxProfit

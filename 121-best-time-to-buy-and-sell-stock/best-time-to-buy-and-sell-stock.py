class Solution(object):
    def maxProfit(self, prices):
        
        min_prices=[prices[0]]
        max_profit=0
        profit=[]


        for i in range (len(prices)):
            if prices[i]<min_prices:
                min_prices=prices[i]
            profit=prices[i]-min_prices
            if max_profit<profit:
                max_profit=profit    

        
     
        return max_profit


        
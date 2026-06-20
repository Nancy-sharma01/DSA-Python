class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        current=prices[0]
        for i in range(len(prices)):
            current=prices[i]
            if current< min_price:
                min_price=current 
            else:
                profit= current- min_price
                if profit>max_profit:
                    max_profit=profit
                    continue
        
        return max_profit  

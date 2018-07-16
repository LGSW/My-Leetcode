class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0 or  len(prices) == 1:
            return 0

        minp = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            #minp = prices[i] if prices[i] < minp else minp
            if  prices[i] < minp:
                minp = prices[i]
            profit = (prices[i] - minp) if prices[i] - minp > profit else profit

        return profit


# Test
# --------------------------------------------------

a = Solution()
print (a.maxProfit([7,1,5,3,6,4]))
print (a.maxProfit([7,6,4,3,1]))

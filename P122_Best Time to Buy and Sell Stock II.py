class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0 or len(prices) == 1:
            return 0

        sum = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                sum += (prices[i+1] - prices[i])

        return sum

    # -----------------------------------------------------------------------

    def maxProfit2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) == 0 or len(prices) == 1:
            return 0

        sum = 0
        curmin = prices[0]
        curmax = prices[0]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                curmax = prices[i]
            if prices[i] < prices[i-1] or i == len(prices)-1:
                sum += (curmax -curmin)
                curmin = prices[i]
                curmax = prices[i]

        return sum



# Test
# ----------------------------------------------------------------------

x  = Solution()
print(x.maxProfit2([7,1,5,3,6,4]))
print(x.maxProfit2([1,2,3,4,5]))
print(x.maxProfit2([7,6,4,3,1]))

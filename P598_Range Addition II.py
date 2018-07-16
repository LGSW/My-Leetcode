class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        sum1 = 9999999; sum2 = 9999999
        for i in ops:
            sum1 = min(sum1, i[0])
            sum2 = min(sum2, i[1])
        return min(sum1, m) * min(sum2, n)

x = Solution()
print(x.maxCount(3,3,[[2,2],[3,3]]))

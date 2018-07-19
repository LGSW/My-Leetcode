class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        re = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                re[j] = re[j-1] + re[j]
        return re[-1]

x = Solution()
print(x.uniquePaths(3,2))
print(x.uniquePaths(7,3))
print(x.uniquePaths(5,5))

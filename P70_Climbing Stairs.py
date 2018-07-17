class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        a = 1; b = 2
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return c

x = Solution()
print(x.climbStairs(3))
print(x.climbStairs(4))
print(x.climbStairs(5))
print(x.climbStairs(6))
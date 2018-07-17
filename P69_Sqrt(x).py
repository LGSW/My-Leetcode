class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)

x = Solution()
print(x.mySqrt(1))
print(x.mySqrt(2))
print(x.mySqrt(8))
print(x.mySqrt(121))

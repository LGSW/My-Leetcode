class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left = 1; right = x
        while(True):
            mid = left + (right - left) // 2
            if (mid > x // mid):
                right = mid - 1
            else:
                if (mid + 1 > x//(mid + 1)):
                    return mid
                left = mid + 1

    def mySqrt2(self, x):

        return int(x**0.5)

x = Solution()
print(x.mySqrt(1))
print(x.mySqrt(2))
print(x.mySqrt(8))
print(x.mySqrt(9))
print(x.mySqrt(10))
print(x.mySqrt(121))

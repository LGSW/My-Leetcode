# o log(n)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        elif n == 1:
            return x

        ispositive = 1
        if n < 0:
            n = n * (-1)
            ispositive = 0

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            result = half * half
        else:
            result = x * half * half

        if ispositive == 1:
            return result
        else:
            return 1/result


# Test

a = Solution()
print(a.myPow(2.01, -10))
print(a.myPow(0.00001, 214748367))

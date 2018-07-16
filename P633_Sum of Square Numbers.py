class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        num = int(c**0.5)
        while(num>=0):
            k = int((c - num*num)**0.5)
            if k*k == (c - num*num):
                return True
            if k > num:
                break
            num -= 1
        return False



x = Solution()
print(x.judgeSquareSum(0))
print(x.judgeSquareSum(1))
print(x.judgeSquareSum(3))
print(x.judgeSquareSum(5))
print(x.judgeSquareSum(25))
print(x.judgeSquareSum(104))
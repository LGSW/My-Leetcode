class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while(n>=1):
            n = n // 5
            cnt += n
        return cnt



a = Solution()
print(a.trailingZeroes(1))
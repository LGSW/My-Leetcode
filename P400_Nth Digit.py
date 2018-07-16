class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        sum = 0
        while(n >= sum):
            add = (10**(x+1) - 10**(x)) * (x+1)
            sum += add
            x += 1
        #print(x)
        w = n - sum + add
        y = w % x
        c = w // x


        return c%(x-y)//(10**y)

x = Solution()
print(x.findNthDigit(10))
print(x.findNthDigit(11))
print(x.findNthDigit(12))
print(x.findNthDigit(13))

# 1234567891011121314151617181920
# 100101012103104
# 100010011002100310041005
# 1134113511361137113811391140
# 1267126812691270
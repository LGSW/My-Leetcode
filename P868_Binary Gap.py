class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        binstr = str(bin(N))[2:]
        idx = -1; result = 0
        for i in range(len(binstr)):
            if binstr[i] == '1':
                if idx != -1:
                    result = max(i - idx, result)
                idx = i
        return result

x = Solution()
print(x.binaryGap(22))
print(x.binaryGap(5))
print(x.binaryGap(6))
print(x.binaryGap(8))
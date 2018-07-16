class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = bin(num)[2:]
        y = '1' * (len(x))
        return (int(x, 2) ^ int(y, 2))

    def findComplement2(self, num):
        i = 1
        while num >= i:
            num ^= i
            i <<= 1
        return num

x  = Solution()
print(x.findComplement(5))  #5(101) -> 2(010)

print(x.findComplement2(5))  #5(101) -> 2(010)
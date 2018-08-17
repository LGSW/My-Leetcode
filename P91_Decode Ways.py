class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        res = [0] * l
        if int(s[0]) != 0:
            res[0] = 1
        else:
            return 0
        for i in range(1,l):
            if int(s[i-1:i+1]) > 0 and int(s[i-1:i+1]) <= 26 and int(s[i-1]) != 0:
                res[i] += res[i-2] if i-2>=0 else 1
            res[i] += res[i-1] if int(s[i])!= 0 else 0

        return res[l-1]

x = Solution()
a = '123'
print(x.numDecodings('0'))
print(x.numDecodings('2002'))
print(x.numDecodings('2'))
print(x.numDecodings('12'))
print(x.numDecodings('226'))
print(x.numDecodings('2262'))
print(x.numDecodings('2272'))
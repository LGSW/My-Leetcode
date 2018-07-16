class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        for i in range(0, len(s), 2 * k):
            s = s[0:i] + s[i:i+k][::-1] + s[i + k:]
        return s

x = Solution()
print(x.reverseStr('abcdefg',2))
print(x.reverseStr('abcde',2))
print(x.reverseStr('abcdefgh',3))

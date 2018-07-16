class Solution(object):
    def findTheDifference(self, s, t):
        x = 0
        for ele in s:
            x ^= ord(ele)
        for ele in t:
            x ^= ord(ele)
        return chr(x)

    def findTheDifference2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        a = dict()
        for c in s:
            if c in a:
                a[c] += 1
            else:
                a[c] = 1
        for c in t:
            if c not in a or a[c] == 0:
                return c
            else:
                a[c] -= 1
        return 0

a = Solution()
print(a.findTheDifference('abcd','abdec'))

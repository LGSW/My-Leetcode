class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        n = len(S)
        res = [0 if c == C else n for c in S]
        for i in range(n - 1): res[i + 1] = min(res[i + 1], res[i] + 1)
        for i in range(n - 1)[::-1]: res[i] = min(res[i], res[i + 1] + 1)
        return res

    def shortestToChar1(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        c = []
        for i, v in enumerate(S):
            if v == C:
                c.append(i)
        r = []
        for i in range(len(S)):
            r.append(min([abs(t - i) for t in c]))
        return r

x = Solution()
print(x.shortestToChar("loveleetcode", "e"))
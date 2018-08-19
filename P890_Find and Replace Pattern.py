class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for w in words:
            f = True; dic1 ={}; dic2 = {}
            for j in range(len(w)):
                if pattern[j] not in dic1:
                    dic1[pattern[j]] = w[j]
                if w[j] not in dic2:
                    dic2[w[j]] = pattern[j]
                if dic1[pattern[j]] != w[j] or dic2[w[j]] != pattern[j]:
                        f = False
                        break
            if f:
                res.append(w)

        return res

x = Solution()
print(x.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],  "abb"))
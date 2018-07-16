class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
        s2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
        s3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])
        res = []
        for w in words:
            if set(list(w.lower())) - s1 == set() or set(list(w.lower())) - s2 == set() or set(
                    list(w.lower())) - s3 == set():
                res.append(w)
        return res


x = Solution()
print(x.findWords(["Hello", "Alaska", "Dad", "Peace"]))
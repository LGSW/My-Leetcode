class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        r = (A + ' ' +B).split(' ')
        dic = dict()
        for w in r:
            if w not in dic:
                dic[w] = 1
            else:
                dic[w] += 1
        re = []
        for x in dic:
            if dic[x] == 1:
                re.append(x)
        return re


x = Solution()
print(x.uncommonFromSentences("this apple is sweet", "this apple is sour"))
print(x.uncommonFromSentences("apple apple", "banana"))
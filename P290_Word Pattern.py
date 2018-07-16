class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        dict1 = dict()
        strlist = str.split(' ')
        if len(pattern) != len(strlist):
            return False

        for p,s in zip(pattern, strlist):
            if p not in dict1:
                if s not in dict1.values():
                    dict1[p] = s
                else:
                    return False
            else:
                if dict1[p] == s:
                    pass
                else:
                    return False
        return True



x = Solution()
print(x.wordPattern('aa','dog dog'))
print(x.wordPattern('aba','dog cat dog'))
print(x.wordPattern('aab','dog cat dog'))

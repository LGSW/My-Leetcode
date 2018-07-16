class Solution:
    def isIsomorphic(self, s, t):
        dict1 =dict()
        for char_s, char_t in zip(s, t):
            if char_s not in dict1:
                if char_t not in dict1.values():
                    dict1[char_s] = char_t
                else:
                    return False
            else:
                if char_t == dict1[char_s]:
                    pass
                else:
                    return False
        return True

    def isIsomorphic2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        ls = len(s)
        lt = len(t)
        if (ls != lt):
            return False
        sett1 = {}
        sett2 = {}
        for i in range(ls):
            if s[i] not in sett1:
                sett1[s[i]] = t[i]
            if t[i] not in sett2:
                sett2[t[i]] = s[i]
            if sett1[s[i]] != t[i] or sett2[t[i]] != s[i]:
                return False

        return True


x = Solution()
print(x.isIsomorphic('egg','add'))
print(x.isIsomorphic('foo','bar'))
print(x.isIsomorphic('paper','title'))
print(x.isIsomorphic('ab','aa'))

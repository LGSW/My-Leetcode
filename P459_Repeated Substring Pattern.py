class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        j = 1
        while(j <= len(s)//2):
            sub = s[0:j]
            if len(s)% len(sub) ==0:
                p = len(s)//len(sub)
                if sub * p == s:
                    return True
            j+=1
        return False

    def repeatedSubstringPattern2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 == 0:
            j = len(s) // 2
        else:
            j = len(s) // 3
        while(j >= 1):
            sub = s[0:j]
            if len(s)% len(sub) ==0:
                p = len(s)//len(sub)
                if sub * p == s:
                    return True
            j-=1
        return False

    def repeatedSubstringPattern3(self, str):

        """
        :type str: str
        :rtype: bool
        """
        if not str:
            return False

        ss = (str + str)[1:-1]
        return ss.find(str) != -1

x = Solution()
print(x.repeatedSubstringPattern3('abab'))
print(x.repeatedSubstringPattern3('abcab'))
print(x.repeatedSubstringPattern3('abcabc'))
print(x.repeatedSubstringPattern3('ababcabab'))
print(x.repeatedSubstringPattern3('ababcababc'))

                
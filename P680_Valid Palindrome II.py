class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while (left < right and s[left] == s[right]):
            left += 1; right -= 1
        if right - left <= 1:
            return True
        if s[left:right] == s[left:right][::-1] or s[left+1:right+1] == s[left+1:right+1][::-1]:
            return True
        return False

    def validPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def parlindrome(s):
            while(len(s) >= 1 and s[0] == s[-1]):
                s = s[1:-1]
            if len(s) <= 1:
                return (s, True)
            return (s, False)
        s, result = parlindrome(s)
        if result:
            return True
        s1, r1 = parlindrome(s[1:])
        s2, r2 = parlindrome(s[:-1])
        if r1 or r2:
            return True
        return False


x = Solution()
print(x.validPalindrome('abc'))
print(x.validPalindrome('eddze'))
print(x.validPalindrome('x'))
print(x.validPalindrome('xx'))
print(x.validPalindrome('xabx'))
print(x.validPalindrome('xabax'))
print(x.validPalindrome('xabcbccax'))
print(x.validPalindrome('xabcx'))
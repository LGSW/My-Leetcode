import re

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == None or s == '':
            return True

        i = 0; j = len(s)-1
        while( i<= j):

            while i>=0 and i < len(s) and not (s[i] >= 'a' and s[i] <= 'z') and not (s[i]>='A' and s[i]<='Z') and not (s[i]>='0' and s[i]<='9'):
                i += 1
            while j>=0 and j < len(s) and not (s[j] >= 'a' and s[j] <= 'z') and not (s[j]>='A' and s[j]<='Z') and not (s[j]>='0' and s[j]<='9'):
                j -= 1

            if i >= len(s) or j < 0:
                return True

            x = s[i]; y = s[j]

            if ord(x)>= ord('a') and ord(x) <= ord('z'):
                x = chr(ord(s[i]) - ord('a') + ord('A'))

            if ord(y)>= ord('a') and ord(y) <= ord('z'):
                y = chr(ord(s[j]) - ord('a') + ord('A'))

            if x == y:
                i += 1; j -= 1
            else:
                return False

        return True




    def isPalindrome2(self, s):
        """
                :type s: str
                :rtype: bool
                """
        s = s.lower()
        s = re.sub('[^a-zA-Z0-9]', '', s)
        return s == s[::-1]


a = Solution()
print("A man, a plan, a canal: Panama", a.isPalindrome2("A man, a plan, a canal: Panama"))
print("aba", a.isPalindrome2("aba"))
print(" ", a.isPalindrome2(" "))

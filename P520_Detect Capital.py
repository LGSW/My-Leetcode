class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.islower() == True or word.isupper() == True:
            return True
        elif word[0].isupper()== True and word[1:].islower() == True:
            return True
        return False

x = Solution()
print(x.detectCapitalUse("USA"))
print(x.detectCapitalUse("Flag"))
print(x.detectCapitalUse("flaG"))


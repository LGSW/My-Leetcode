class Solution(object):
    def reverseWords(self, s):
        words = s.split(' ')
        return ''.join(w[::-1] + ' ' for w in words)[:-1]

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        result = ''
        for word in words:
            result += word[::-1]+' '
        return result[:-1]

x = Solution()
print(x.reverseWords("Let's take LeetCode contest"))
print(x.reverseWords1("Let's take LeetCode contest"))
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = [1]
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                group[-1] += 1
            else:
                group.append(1)
        return sum(min(group[i],group[i-1]) for i in range(1,len(group)))

x = Solution()
print(x.countBinarySubstrings("00110011"))
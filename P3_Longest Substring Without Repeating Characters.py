class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = 0; ed = 0; lonstr = ''
        maxlen = 0;
        while(ed < len(s)):
            if s[ed] not in lonstr:
                lonstr += s[ed]
                ed += 1;
            else:
                p = lonstr.index(s[ed])
                maxlen = max(ed - st, maxlen)
                lonstr = lonstr[p+1:] + s[ed]
                st += p+1; ed += 1
        return max(len(lonstr),maxlen)

    def lengthOfLongestSubstring2(self, s):
        ans = 0; i = 0
        indx =[0]* 128
        for j in range(0, len(s)):
            i = max(indx[ord(s[j])], i)
            ans = max(ans, j - i + 1)
            indx[ord(s[j])] = j + 1
        return ans


x = Solution()
print(x.lengthOfLongestSubstring2("abcabcbb"))
print(x.lengthOfLongestSubstring2("bbbb"))
print(x.lengthOfLongestSubstring2("pwwkew"))
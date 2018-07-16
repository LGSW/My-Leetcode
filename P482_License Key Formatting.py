class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.upper().replace('-', '')
        size = len(S)
        s1 = K if size % K == 0 else size % K
        res = S[:s1]
        while s1 < size:
            res += '-' + S[s1:s1 + K]
            s1 += K
        return res

    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        newstr = ''; l =0
        for i in range(len(S))[::-1]:
            ch = S[i]
            if ch == '-':
                continue
            elif ord(ch)>= ord('a') and ord(ch)<=ord('z'):
                ch = chr(ord(ch)-ord('a')+ord('A'))
            newstr = ch + newstr; l += 1
            if l % K == 0:
                newstr = '-' + newstr
        if newstr != '' and newstr[0] == '-':
            newstr = newstr[1:]
        return newstr


ex = Solution()
print(ex.licenseKeyFormatting('5F3Z-2e-9-w',4))
print(ex.licenseKeyFormatting('2-5g-3-J',2))
print(ex.licenseKeyFormatting('---',3))

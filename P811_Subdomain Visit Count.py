class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dic = {}
        for cp in cpdomains:
            a = cp.split(' ')
            s = a[1].split('.')
            num = int(a[0])
            strs = ''
            for i in range(len(s))[::-1]:
                if i != len(s) -1:
                    strs = s[i] +  '.' + strs
                else:
                    strs = s[i]
                if strs not in dic:
                    dic[strs] = num
                else:
                    dic[strs] += num
        result = []
        for i in dic:
            result.append(str(dic[i]) + ' ' + i)
        return result


x = Solution()
print(x.subdomainVisits(["9001 discuss.leetcode.com"]))
print(x.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
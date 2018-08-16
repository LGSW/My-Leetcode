class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2,3,5,7,11,13,17,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103]
        dic = {}; res = []; l = 0
        for s in strs:
            re = 1
            for ch in s:
                re = re * prime[ord(ch) - ord('a')]
            if re not in dic:
                dic[re] = l; l += 1
                res.append([s])
            else:
                res[dic[re]].append(s)
        return res

    def groupAnagrams2(self, strs):
        f = []; res =[]
        for str in strs:
            x = sorted(list(str))
            if x not in f:
                f.append(x)
                res.append([str])
            else:
                k = f.index(x)
                res[k].append(str)
        return res

x = Solution()
print(x.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(x.groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))

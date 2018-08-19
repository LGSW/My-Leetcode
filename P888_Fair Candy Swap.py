class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ss = (sum(A) + sum(B))// 2
        dic = dict(); c = sum(A) - ss
        for i in A:
            dic[i-c] = i
        for i in B:
            if i in dic:
                return [dic[i], i]
        return 0

x = Solution()
print(x.fairCandySwap([1,2,5],[2,4]))
print(x.fairCandySwap([1,1],[2,2]))

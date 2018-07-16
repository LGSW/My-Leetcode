class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        print(sum(matrix, []))
        return sorted(sum(matrix, []))[k-1]

x = Solution()
print(x.kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
# 1  5  9
# 10 11 13
# 12 13 15
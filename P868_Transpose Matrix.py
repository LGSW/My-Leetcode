class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(A[0])):
            result.append([])
            for j in range(len(A)):
                result[i].append(A[j][i])
        return result

x = Solution()
print(x.transpose([[1,2,3],[4,5,6],[7,8,9]]))
print(x.transpose([[1,2,3],[4,5,6]]))
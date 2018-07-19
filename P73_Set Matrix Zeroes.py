class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0]); n = len(matrix)
        col1 = 1
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if j == 0:
                        col1 = 0
                    else:
                        matrix[0][j] = 0
                    matrix[i][0] =0
        for i in range(n)[1:]:
           if matrix[i][0] == 0:
               matrix[i] = [0] * m
        for j in range(m)[1:]:
            if matrix[0][j] == 0:
                for i in range(n):
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            matrix[0] = [0] * m
        if col1 == 0:
            for i in range(n):
                matrix[i][0] = 0

        # return matrix

x = Solution()
print(x.setZeroes([[0,1,2,0],
                  [3,4,5,2],
                  [1,3,1,5]]))
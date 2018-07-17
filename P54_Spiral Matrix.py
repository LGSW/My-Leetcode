class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or matrix == []:
            return matrix
        row = len(matrix[0]); col = len(matrix) - 1
        x = 0; y = 0
        result = []
        while(row > 0 or col > 0):
            for i in range(row):
                result.append(matrix[y][x+i])
            if row <= 0 or col <= 0:
                break
            row -= 1; x += row ; y += 1
            for i in range(col):
                result.append(matrix[y+i][x])
            if row <= 0 or col <= 0:
                break
            col -= 1; x -= 1; y += col
            for i in range(row):
                result.append(matrix[y][x-i])
            if row <= 0 or col <= 0:
                break
            row -= 1; x -= row; y -= 1
            for i in range(col):
                result.append(matrix[y-i][x])
            if row <= 0 or col <= 0:
                break
            col -= 1; x += 1; y -= col
        return result


x = Solution()
print(x.spiralOrder([[ 1, 2, 3 ],
                    [ 4, 5, 6 ],
                    [ 7, 8, 9 ]]))
print(x.spiralOrder([[1, 2, 3, 4, 5],
                    [6, 7, 8, 9, 10],
                    [11,12, 13, 14,15]]))
print(x.spiralOrder([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9,10,11,12]]))
print(x.spiralOrder([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9,10,11,12],
                    [13,14,15,16]]))
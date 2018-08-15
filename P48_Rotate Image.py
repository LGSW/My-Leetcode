class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        i = 0; left = 0; right = l - 1
        while(right - left >= 0):
            for j in range(left, right):
                x = matrix[i][j]
                matrix[i][j] = matrix[l - 1 - j][i]
                matrix[l - 1 - j][i] = matrix[l - 1 - i][l - 1 - j]
                matrix[l - 1 - i][l - 1 - j] = matrix[j][l - 1 - i]
                matrix[j][l - 1 - i] = x
            i += 1; left += 1; right -= 1
        #return matrix

x = Solution()
print(x.rotate([
  [1,2],
  [3,4]]))
print(x.rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]]))
print(x.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))

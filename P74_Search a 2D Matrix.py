class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                left = 0; right = len(matrix[i]) - 1
                while(left <= right):
                    mid = (left + right)// 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                return False
        return False

    def searchMatrix2(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        for i in range(len(matrix)):
            if target == matrix[i][-1]:
                return True
            elif target < matrix[i][-1]:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target: return True
                return False
        return False



x = Solution()
print(x.searchMatrix([[1, 3, 5]], 1))
print(x.searchMatrix([[1, 3, 5, 7],
                     [10, 11, 16, 20],
                     [23, 30, 34, 50]], 13))
print(x.searchMatrix([[1, 3, 5, 7],
                     [10, 11, 16, 20],
                     [23, 30, 34, 50]], 3))
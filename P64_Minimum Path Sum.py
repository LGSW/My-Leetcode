class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        m = len(grid[0]); n = len(grid)
        re = [[0 for i in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if i-1 >= 0 and j-1 >= 0:
                    re[i][j] = min(re[i-1][j], re[i][j-1]) + grid[i][j]
                elif i-1 >=0 and j-1 < 0:
                    re[i][j] = re[i-1][j] + grid[i][j]
                elif j-1 >=0 and i-1 < 0:
                    re[i][j] = re[i][j - 1] + grid[i][j]
                else:
                    re[i][j] = grid[i][j]
        return re[n-1][m-1]

x = Solution()
print(x.minPathSum([[1,3,1],
                    [1,5,1],
                    [4,2,1]]))


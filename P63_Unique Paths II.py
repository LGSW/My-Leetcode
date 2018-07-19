class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if len(obstacleGrid) == 0:
            return 0
        n = len(obstacleGrid); m = len(obstacleGrid[0])
        re = [1] + [0] * (m-1)
        for i in range(n):
            if obstacleGrid[i][0] == 1:
                re [0] = 0
            for j in range(1 , m):
                if obstacleGrid[i][j] != 1:
                    re[j] = re[j - 1] + re[j]
                else:
                    re[j] = 0
        return re[-1]

x = Solution()
print(x.uniquePathsWithObstacles([[0,0,0],
                                  [0,1,0],
                                  [0,0,0]]))
print(x.uniquePathsWithObstacles([[0,0,0,0],
                                  [0,1,0,0],
                                  [0,0,0,0]]))
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for i in range(n)]
        num = 1
        row = n; col = n - 1
        x = 0; y = 0;
        while(num <= n**2):
            for i in range(row):
                result[y][x+i] = num
                num += 1
            if num > n**2: break
            row -= 1; x += row; y += 1
            for i in range(col):
                result[y+i][x] = num
                num += 1
            if num > n**2: break
            col -= 1; y += col; x -= 1
            for i in range(row):
                result[y][x-i] = num
                num += 1
            if num > n**2: break
            row -= 1; x -= row; y -= 1
            for i in range(col):
                result[y - i][x] = num
                num += 1
            if num > n ** 2: break
            col -= 1; y -= col; x += 1;

        return result

x = Solution()
print(x.generateMatrix(4))
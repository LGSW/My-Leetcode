class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        rows = [[1]]

        if numRows == 1:
            return rows

        rows.append([1,1])

        if numRows == 2:
            return rows

        for i in range(2,numRows):
            rows.append([1])
            for j in range(1,i):
                a = rows[i-1][j-1] + rows[i-1][j]
                rows[i].append(a)
            rows[i].append(1)

        return rows
# Test

x = Solution()
print( x.generate(6) )

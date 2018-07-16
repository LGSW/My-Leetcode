class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        rows = [1,1]
        for i in range(1,rowIndex):
            for j in range(len(rows)-1):
                rows[j] = rows[j] + rows[j+1]
            rows.insert(0,1)
        return rows


# Test
# ---------------------------------------

a = Solution()
print(a.getRow(4))


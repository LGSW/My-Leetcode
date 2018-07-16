class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        leng = len(triangle)

        if leng == 0:
            return 0

        if leng == 1:
            return triangle[0][0]

        for i in range(1,leng):
            for j in range(len(triangle[i])):
                if j-1 < 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i - 1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j-1] if triangle[i-1][j-1] < triangle[i-1][j] else triangle[i-1][j]

            #print(triangle[i])

        min = 9999999
        for i in range(len(triangle[leng-1])):
            if triangle[leng-1][i] <min:
                min = triangle[leng-1][i]

        return min


# Test
#-----------------------------------------------------------------

x = Solution()
print(x.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))

print(x.minimumTotal([[10]]))
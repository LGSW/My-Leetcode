import math

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        L = len(M); W = len(M[0])

        N = [[0] * W for i in range(L)]

        for i in range(L):
            for j in range(W):
                sum = 0; cnt = 0
                for x in [i-1,i,i+1]:
                    for y in [j-1,j,j+1]:
                        if x >= 0 and x < L and y >= 0 and y < W :
                            sum += M[x][y]
                            cnt += 1
                # print(i,j,sum,cnt)
                N[i][j] = (int)(math.floor(sum/cnt))

        return N



        '''
        N = M
        N[0][0] = (N[0][0] + N[0][1] + N[1][0] + N[1][1]) / 4
        N[0][len(M)-1] = (N[0][len(M)-1] + N[0][(len(M)-2)] + N[1][len(M)-1] + N[1][len(M)-2]) / 4
        N[len(M)-1][0] = (N[len(M)-1][0] + N[len(M)-1][1] + N[len(M)-2][0] + N[len(M)-2][1]) / 4
        N[len(M)-1][len(M)-1] = (N[len(M)-1][len(M)-1] + N[len(M)-1][len(M)-2] + N[len(M)-2][len(M)-1] + N[len(M)-2][len(M)-2]) / 4

        for i in range(len(M)):
            for j in range(len(M[i])):
                if (i==0 or i==len(M)-1) and (j==0 or j==len(M)-1):
                    continue
                elif i==0:
                    N[i][j] = (N)
        '''

a = Solution()
arr = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
# arr = [[2,3]]
print(a.imageSmoother(arr))
class Solution(object):

    def islandPerimeter(self, grid):
        ans = 0
        for i, r in enumerate(grid):
            print(i,r)
            for j, c in enumerate(r):
                print(j,c)
                if c:
                    ans += 4
                    if i > 0 and grid[i - 1][j]: ans -= 2
                    if j > 0 and grid[i][j - 1]: ans -= 2
        return ans

    def islandPerimeter1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        s = 0
        count = 0
        for i in range(len(grid)):
            count += sum(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] ==1:
                    if i+1 < len(grid):
                        s += grid[i][j]&grid[i+1][j]
                    if j+1 < len(grid[i]):
                        s += grid[i][j]&grid[i][j+1]
        return count*4 - s*2

    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            if grid[i].count(1) > 0:
                break
        if i == len(grid): return 0
        for j in range(len(grid[i])):
            if grid[i][j]==1:
                break

        new = [(i,j)]; used =[(i,j)]
        count = 0; sum = 0
        while(new != []):
            (i, j) = new.pop(0)
            count += 1
            if j - 1 >= 0 and grid[i][j-1] == 1:
                sum += 1
                if (i,j-1)not in used:
                    new.append((i,j-1)); used.append((i,j-1))
            if j + 1 < len(grid[0]) and grid[i][j+1] == 1:
                sum += 1
                if (i,j+1)not in used:
                    new.append((i,j+1)); used.append((i,j+1))
            if i - 1 >= 0 and grid[i-1][j] == 1:
                sum += 1
                if (i-1,j) not in used:
                    new.append((i-1,j)); used.append((i-1,j))
            if i + 1 < len(grid) and grid[i+1][j] == 1:
                sum += 1
                if (i+1,j)not in used:
                    new.append((i+1,j)); used.append((i+1,j))
        return count*4 - sum


    def islandPerimeter3(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        w = len(grid)
        l = len(grid[0])
        per = 0
        for i in range(w):
            for j in range(l):
                if grid[i][j] == 1:
                    if j-1 < 0 or grid[i][j-1]==0: per += 1
                    if j+1 >= l or grid[i][j+1]==0: per += 1
                    if i-1 < 0 or grid[i-1][j]==0: per += 1
                    if i+1 >= w or grid[i+1][j]==0: per += 1
                    #print(i,j, s)
        return per

x = Solution()
island = [[0,1,0,0],
          [1,1,1,0],
          [0,1,0,0],
          [1,1,0,0]]

island2 = [[1,1],
           [1,1]]

island3 = [[0,1,1],
           [1,1,0]]

print(x.islandPerimeter(island))
print(x.islandPerimeter(island2))
print(x.islandPerimeter(island3))
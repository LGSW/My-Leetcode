import math

class Solution(object):
    def constructRectangle(self, area):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(int(math.sqrt(area))+1)[::-1]:
            if area % i == 0:
                return [area//i, i]
        return [area, 1]


x = Solution()
print(x.constructRectangle(25))
print(x.constructRectangle(24))
print(x.constructRectangle(23))
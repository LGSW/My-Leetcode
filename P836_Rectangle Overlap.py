class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        x1 = rec1[0]; y1 = rec1[1]
        x2 = rec1[2]; y2 = rec1[3]
        x3 = rec2[0]; y3 = rec2[1]
        x4 = rec2[2]; y4 = rec2[3]
        if ((min(x2, x4) - max(x1, x3) > 0) and (min(y2, y4) - max(y1, y3) > 0)):
            return True
        return False

x = Solution()
print(x.isRectangleOverlap([0,0,2,2], [1,1,3,3]))
print(x.isRectangleOverlap([0,0,1,1], [1,0,2,1]))
print(x.isRectangleOverlap([0,0,1,1], [2,2,3,3]))
print(x.isRectangleOverlap([7,8,13,15], [10,8,12,20]))
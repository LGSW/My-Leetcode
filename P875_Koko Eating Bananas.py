import math
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        p = sorted(piles)
        for i in range(1,p[-1]):
            sum = 0
            for n in piles:
                sum += math.ceil(n/i)
            if sum <= H:
                return i
        return p[-1]


x = Solution()
print(x.minEatingSpeed([3], 8))
print(x.minEatingSpeed([3,6,7,11], 8))
print(x.minEatingSpeed([30,11,23,4,20], 5))
print(x.minEatingSpeed([30,11,23,4,20], 6))
print(x.minEatingSpeed([332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184],823855818))
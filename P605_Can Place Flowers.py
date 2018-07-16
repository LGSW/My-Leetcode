class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i, x in enumerate(flowerbed):
            if (not x and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)):
                n -= 1
                flowerbed[i] = 1
        return n <= 0

    def canPlaceFlowers1(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        sum = 0; i = 0
        while(i < len(flowerbed) and flowerbed[i] == 0): i += 1
        sum += i // 2
        if i == len(flowerbed):
            return ((len(flowerbed)+1)//2 >= n)
        j = len(flowerbed)- 1
        while (j >= 0 and flowerbed[j] == 0): j -= 1
        sum += (len(flowerbed) - 1 - j) // 2
        if sum >= n:
            return True
        s = 0
        for k in flowerbed[i:j+1]:
            if k == 0:
                s+= 1
            else:
                if s != 0:
                    sum += (s-1)//2
                    if sum >= n:
                        return True
                s = 0
        return False

x = Solution()
print(x.canPlaceFlowers([0],1))
print(x.canPlaceFlowers([0,0,0],2))
print(x.canPlaceFlowers([1,0,0,0,1],1))
print(x.canPlaceFlowers([1,0,0,0,1],2))
print(x.canPlaceFlowers([0,0,1,0,1],1))
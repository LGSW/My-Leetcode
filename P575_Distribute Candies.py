class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        dic = dict()
        for candy in candies:
            if candy not in dic:
                dic[candy] = 1
            else:
                dic[candy] += 1
        if (len(dic) > len(candies)/2):
            return len(candies)//2
        else:
            return len(dic)


x = Solution()
print(x.distributeCandies([1,1,2,3]))
print(x.distributeCandies([1,1,1,1,2,2,3,3]))
print(x.distributeCandies([1,1,1,5,2,2,3,3]))
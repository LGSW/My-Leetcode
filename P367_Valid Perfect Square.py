class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low = 1; high = num
        while (low <= high):
            mid = (low + high) >> 1
            if (mid * mid == num):
                return True;
            elif mid * mid < num:
                low = mid + 1
            else:
                high = mid - 1
        return False


    def isPerfectSquare2(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while(num >0):
            num -= i
            i += 2
        return num == 0

    def isPerfectSquare3(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while(x * x > num):
            x = (x + num//x) >> 1
        return x * x ==num



x = Solution()
print(x.isPerfectSquare3(9))
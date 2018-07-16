class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        result = [True] * n
        result[0] = result[1] = False;
        for i in range(2, n):
            if result[i] == True:
                for j in range(i, (n-1)//i+1):
                    result[i*j] = False
        return sum(result)

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n < 3:
            return 0
        elif n ==3:
            return 1
        elif n ==4 or n ==5:
            return 2
        pl = [2, 3]
        cnt = 2
        for i in range(5, n, 2):
            x = 0
            for j in pl[1:]:
                if i % j == 0:
                    break
                if j*j >= i:
                    pl.append(i)
                    cnt += 1
                    break

        return cnt

a = Solution()
print(a.countPrimes(49979))
print(a.countPrimes2(49979))
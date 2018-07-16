class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 6:
            return True
        sum1 = 0
        for i in range(1, int(num**0.5)):
            if num % i == 0:
                sum1 = sum1 + i
                if (i * i != num):
                    sum1 = sum1 + num / i
        return ((sum1 - num) == num)

    def checkPerfectNumber1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        arr = [1]
        n = num
        sum = 1
        for p in range(2, n//2+1):
            k = 0
            while(n % p ==0):
                n = n // p
                k += 1
            newarr =[]
            for i in range(k):
                for j in arr:
                    x = p**(i+1) * j
                    sum += x
                    newarr.append(x)
            arr = arr + newarr
            if p * p >= n:
                break
        if n != 1:
            newarr = []
            for j in arr:
                x = n * j
                sum += x
                newarr.append(x)
            arr = arr + newarr
        #print(arr, sum, num)
        return sum == 2*num

x = Solution()
print(x.checkPerfectNumber1(1))
print(x.checkPerfectNumber1(6))
print(x.checkPerfectNumber1(28))
print(x.checkPerfectNumber1(20996011))


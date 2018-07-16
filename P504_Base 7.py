class Solution(object):
    def convertToBase7(self, num):
        """
            :type num: int
            :rtype: str
        """
        ns = '-' if num<0 else '0' if num==0 else ''
        l , num = '', abs(num)
        while(num > 0):
            l = str(num % 7) + l
            num = num //7
        return ns + l

    def convertToBase7x(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num > 0:
            nums = num; f = 0
        else:
            nums = -num; f = 1
        num = nums
        count = 0
        while(num != 0):
            num = num // 7
            count += 1
        ns = ''
        for i in range(count)[::-1]:
            k = nums // (7**i)
            ns =  ns + str(k)
            nums = nums - k*7**i
        if f==0:
            return ns
        else:
            return '-'+ns

x = Solution()
print(x.convertToBase7(1))
print(x.convertToBase7(-49))
print(x.convertToBase7(15))
print(x.convertToBase7(-15))
print(x.convertToBase7(100))


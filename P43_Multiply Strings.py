class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1))[::-1]:
            k = len(num1) - 1 - i
            for j in range(len(num2))[::-1]:
                temp1 = 0
                ts = int(num1[i]) * int(num2[j])
                result[k] +=  ts % 10
                temp1 = result[k] // 10; result[k] %= 10
                result[k + 1] += ts // 10 + temp1
                k += 1
        pt = len(num1) + len(num2) - 1
        while pt > 0 and result[pt] == 0:
            pt -= 1
        result = result[:pt+1]
        result.reverse()
        return ''.join(map(str,result))

x = Solution()
print(x.multiply("1", "1"))
print(x.multiply("3", "4"))
print(x.multiply("11", "11"))
print(x.multiply("99", "99"))
print(x.multiply("111", "111"))
print(x.multiply("123", "456"))
print(x.multiply("324", "456"))
print(x.multiply("999", "999"))
print(x.multiply("9133", "0"))

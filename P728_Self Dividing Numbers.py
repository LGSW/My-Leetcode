class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left,right+1):
            if '0' not in str(i):
                re =True
                for j in str(i):
                    if i % int(j) != 0:
                        re = False
                        break
                if re:
                    result.append(i)
        return result

x = Solution()
print(x.selfDividingNumbers(1,22))
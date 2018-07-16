class Solution:
    def checkRecord(self, s): # 正则表达式
        """
        :type s: str
        :rtype: bool
        """
        return re.match(r".*A.*A|.*LLL.*", s) == None

    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sumA = 0; sumL= 0
        for i in s:
            if i == 'A':
                sumA += 1
                if sumA > 1:
                    return False
            if i =='L':
                sumL += 1
                if sumL > 2:
                    return False
            else:
                sumL = 0
        return True

x = Solution()
print(x.checkRecord('PPALLP'))
print(x.checkRecord('PPALLL'))
print(x.checkRecord('PPALLA'))
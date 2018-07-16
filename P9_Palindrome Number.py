class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        strx=str(x)
        l = len(strx)
        ct = 0
        for i in range(int((l+1)/2)):
            if(strx[i]!=strx[l-1-i]):
                print(i)
                break
            ct+=1
        if(ct== int((l+1)/2)):
            return True
        else:
            return False


a=Solution()
print(a.isPalindrome(-101))



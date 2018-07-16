class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if len(bits) == 1 or bits[-2] == 0:
            return True
        idx = len(bits)-2; sum = 0
        while(idx >= 0 and bits[idx] == 1):
            idx -= 1
            sum += 1
        if sum%2 == 1:
            return False
        return True

    def isOneBitCharacter1(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if not bits: return False
        n = len(bits)

        index = 0
        while index < n:
            if index == n - 1: return True
            if bits[index] == 1:
                index += 2
            else:
                index += 1
        return False

x = Solution()
print(x.isOneBitCharacter([1, 1, 1, 0]))
print(x.isOneBitCharacter([1, 1, 0]))
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        x = -(-len(B) // len(A))
        if B in A * x:
            return x
        elif B in A * (x + 1):
            return x + 1
        return -1

    def repeatedStringMatch1(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        t = -(-len(B) // len(A))  # Equal to ceil(len(b) / len(a))
        return t * (B in A * t) or (t + 1) * (B in A * (t + 1)) or -1

x = Solution()
#print('ab' in 'abvcd')
print(x.repeatedStringMatch("abcd","cdabcdab"))
print(x.repeatedStringMatch("abababaaba","aabaaba"))
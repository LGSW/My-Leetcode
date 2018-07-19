import math
class Solution:
    """
    :type n: int
    :type k: int
    :rtype: str
    """
    def getPermutation(self, n, k):
        numbers = [i for i in range(1,n+1)]
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation


x = Solution()
print(x.getPermutation(3,3))
print(x.getPermutation(4,9))
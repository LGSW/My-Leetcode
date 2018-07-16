import itertools

class Solution(object):

    klist = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,
     1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]

    klist2 = [[1], [2], [4], [8], [1, 6], [2, 3], [4, 6], [1, 2, 8], [2, 5, 6], [1, 2, 5], [0, 1, 2, 4], [0, 2, 4, 8],
     [0, 4, 6, 9], [1, 2, 8, 9], [1, 3, 4, 6, 8], [2, 3, 6, 7, 8], [3, 5, 5, 6, 6], [0, 1, 1, 2, 3, 7],
     [1, 2, 2, 4, 4, 6], [2, 2, 4, 5, 8, 8], [0, 1, 4, 5, 6, 7, 8], [0, 1, 2, 2, 5, 7, 9], [0, 1, 3, 4, 4, 4, 9],
     [0, 3, 6, 8, 8, 8, 8], [1, 1, 2, 6, 6, 7, 7, 7], [2, 3, 3, 3, 4, 4, 5, 5], [0, 1, 4, 6, 6, 7, 8, 8],
     [1, 1, 2, 2, 3, 4, 7, 7, 8], [2, 3, 4, 4, 5, 5, 6, 6, 8], [0, 1, 2, 3, 5, 6, 7, 8, 9],
     [0, 1, 1, 2, 3, 4, 4, 7, 7, 8]]

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        x = []
        while(N > 0):
            chr = N % 10
            x.append(chr)
            N = N // 10
        x.sort()
        print(x)
        if x in self.klist2:
            return True
        return False


    def reorderedPowerOf2_1(self, N):
        """
        :type N: int
        :rtype: bool
        """
        if N == 1:
            return True
        numlist = []
        while(N > 0):
            numlist.append(N % 10)
            N = N // 10
        re = list(itertools.permutations(numlist, len(numlist)))
        used = []
        for i in re:
            if i[0] == 0 or i[-1] % 2 == 1 or i[-1] == 0:
                continue
            num = ''
            for j in i:
                num += str(j)
            if num not in used:
                if self.ifpowof2(int(num)):
                    return True
            else:
                used.append(num)
        return False

    def ifpowof2 (self, n):
        if n < 1: return False
        while(n > 1):
            n = n//2
            if n != 1 and n % 2 == 1:
                return False
        return True

    def createlist(self):
        list = [1]
        a = 1
        while(a<1e9):
            a = a * 2
            list.append(a)
        print(list)

    def adjustlist(self, list):
        result = []
        for i in list:
            n=[]
            while (i > 0):
                n.append(i % 10)
                i = i // 10
            n.sort()
            result.append(n)
        return result

x = Solution()
x.createlist()
re = x.adjustlist(x.klist)
print(re)
print(x.reorderedPowerOf2(1))
print(x.reorderedPowerOf2(2))
print(x.reorderedPowerOf2(3))
print(x.reorderedPowerOf2(4))
print(x.reorderedPowerOf2(10))
print(x.reorderedPowerOf2(46))
print(x.reorderedPowerOf2(821))
print(x.reorderedPowerOf2(26038888))
print(x.reorderedPowerOf2(679213508))
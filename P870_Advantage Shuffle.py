class Solution(object):
    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        dic = {}
        a = sorted(A)
        b = sorted(B)
        st = 0; ed = len(a)-1
        for i in range(len(b))[::-1]:
            if a[ed] > b[i]:
                if b[i] not in dic:
                    dic[b[i]] = [a[ed]]
                else:
                    dic[b[i]].append(a[ed])
                ed -= 1
            else:
                if b[i] not in dic:
                    dic[b[i]] = [a[st]]
                else:
                    dic[b[i]].append(a[st])
                st += 1
        result = []
        for num in B:
            result.append(dic[num].pop())

        return result

x = Solution()
print(x.advantageCount([2,7,11,15], [1,10,4,11]))
print(x.advantageCount([12,24,8,32], [13,25,32,11]))
print(x.advantageCount([2,0,4,1,2], [1,3,0,0,2]))
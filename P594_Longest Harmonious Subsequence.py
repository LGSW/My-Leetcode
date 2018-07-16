import collections

class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        nums.sort()
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        len = 0
        for i in dic:
            if i-1 in dic and dic[i] + dic[i-1] > len:
                len =  dic[i] + dic[i-1]
        return len

    def findLHS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = collections.Counter(nums)
        print(count)
        return max([count[x] + count[x + 1] for x in count if count[x + 1]] or [0])

x = Solution()
print(x.findLHS1([1,3,2,2,5,2,3,7]))
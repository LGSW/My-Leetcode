class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}; maxfreq = 0
        for i,num in enumerate(nums):
            if num in dic:
                dic[num].append(i)
            else:
                dic[num] = [i]
            maxfreq = max(len(dic[num]), maxfreq)
        minlen = 1e9;
        for i in dic:
            if len(dic[i]) == maxfreq:
                minlen = min (minlen, dic[i][-1] - dic[i][0] + 1)
        return minlen

x = Solution()
print(x.findShortestSubArray([1]))
print(x.findShortestSubArray([1, 2, 2, 3, 1]))
print(x.findShortestSubArray([1, 2, 2, 3, 1, 4, 2]))
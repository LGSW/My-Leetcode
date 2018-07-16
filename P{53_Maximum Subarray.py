class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0; sumlist = []
        allpos = False
        for i in nums:
            sum += i
            sumlist.append(sum)
        mins = 0; maxs = -1e12
        for i in sumlist:
            maxs = max(maxs, i - mins)
            mins = min(mins, i)
        return maxs

x = Solution()
print(x.maxSubArray([1]))
print(x.maxSubArray([-1]))
print(x.maxSubArray([1,2,3]))
print(x.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        l = 1; maxl = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                l += 1
            else:
                maxl = max(maxl, l)
                l = 1
        return max(maxl, l)

x = Solution()
print(x.findLengthOfLCIS([1,3,5,4,7]))
print(x.findLengthOfLCIS([2,2,2,2,2]))
print(x.findLengthOfLCIS([1,3,5,7]))

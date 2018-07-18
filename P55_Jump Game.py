class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxreach = 0
        for i in range(len(nums)):
            if i > maxreach:
                return False
            maxreach = max(maxreach, i + nums[i])
            if maxreach >= len(nums) - 1:
                return True
        return True

x = Solution()
print(x.canJump([2,3,1,1,4]))
print(x.canJump([3,2,1,0,4]))
print(x.canJump([3,0,8,2,0,0,1]))
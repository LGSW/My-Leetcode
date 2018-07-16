class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])

        value = [0] * len(nums)
        value[0] = nums[0]
        value[1] = nums[1]
        value[2] = nums[0] + nums[2]

        for i in range(3,len(nums)):
            value[i] = max(value[i-3] , value[i-2]) + nums[i]

        return max(value[len(nums)-1], value[len(nums)-2])

## -------------------------------------------------------------------


    def rob2(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            nums[i] = max(nums[i-2]+ nums[i], nums[i-1])

        return nums[len(nums)-1]


a = Solution()
print([1,2,3,1], a.rob2([1,2,3,1]))
print([2,1,1,2], a.rob2([2,1,1,2]))
print([2,100,9,3,7], a.rob2([2,100,9,3,7]))
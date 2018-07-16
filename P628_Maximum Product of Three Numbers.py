class Solution(object):
    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if nums[-1] <= 0:
            return nums[-3] * nums[-2] * nums[-1]
        else:
            return max(nums[0] * nums[1],nums[-3] * nums[-2]) * nums[-1]

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


x = Solution()
print(x.maximumProduct([1,2,3]))
print(x.maximumProduct([1,2,3,4]))
print(x.maximumProduct([-4,-3,-2,-1,60]))
print(x.maximumProduct([-4,-3,-2,-1,0]))
print(x.maximumProduct([-4,-3,-2,-1]))
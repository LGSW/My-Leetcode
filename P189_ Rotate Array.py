class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[0:-k]

        return nums


x = Solution()
print(x.rotate([1,2,3,4,5,6,7],3))
print(x.rotate([1],0))
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []; l = len(nums)
        if (not nums or l < 4):
            return res
        nums.sort()
        maxnum = nums[-1]
        if (4 * nums[0] > target  or 4 * maxnum < target):
            return res;
        for i in range(0, l):
            z = nums[i]
            if (i > 0 and z == nums[i - 1]):
                continue
            if (z + 3 * maxnum < target):
                continue
            if (4 * z > target):
                break
            if (4 * z == target):
                if (i + 3 < len and nums[i + 3] == z):
                    res.append([z, z, z, z])
                break

        print(nums)

x = Solution()
print(x.fourSum([1,2,4,2],2))

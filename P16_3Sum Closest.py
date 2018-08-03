class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort(); l = len(nums)
        if (nums[l - 3] + nums[l - 2] + nums[l - 1] <= target):
            return nums[l-3] + nums[l-2] + nums[l-1]
        if (nums[0] + nums[1] + nums[2] >= target):
            return nums[0] + nums[1] + nums[2]
        closest = nums[0] + nums[1] + nums[l - 1]
        for s in range(0, l -2):
            if (s != 0 and nums[s - 1] == nums[s]): continue
            if (nums[s] + nums[l - 1] + nums[l - 2] < target and s < l - 3):
                if abs(closest - target) > target - (nums[s] + nums[l - 1] + nums[l - 2]):
                    closest = nums[s] + nums[l - 1] +nums[l - 2]
                continue
            if (nums[s] + nums[s + 1] + nums[s + 2] > target):
                if (abs(closest-target) > (nums[s]+nums[s+1]+nums[s+2])-target):
                    closest = nums[s]+nums[s+1]+nums[s+2]
                break
            newTarget = target - nums[s]
            m = s + 1; b = l - 1
            while (m < b):
                if (nums[m] + nums[b] < newTarget):
                    if abs(closest-target) > newTarget - nums[m] - nums[b]:
                        closest = nums[s]+nums[m]+nums[b]
                    m += 1
                elif (nums[m] + nums[b] > newTarget):
                    if (abs(closest - target) > nums[m] + nums[b] - newTarget):
                        closest = nums[s] + nums[m] + nums[b]
                    b -= 1
                else:
                    return target
        return closest

x = Solution()
print(x.threeSumClosest([-1, 2, 1, -4] , 1))
print(x.threeSumClosest([1, 1, -1, -1, 3] , 1))

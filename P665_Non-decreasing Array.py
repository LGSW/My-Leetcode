class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = 0;
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                s += 1
                if i-2 < 0 or i+1 >= len(nums) or nums[i] > nums[i-2] or nums[i-1] < nums[i+1]:
                    pass
                else:
                    return False
            if s > 1:
                return False
        return True


x = Solution()
print(x.checkPossibility([4,2,3]))
print(x.checkPossibility([4,2,1]))
print(x.checkPossibility([3,4,2,3]))
print(x.checkPossibility([-1,4,2,3]))
print(x.checkPossibility([3,3,2,2]))
print(x.checkPossibility([2,3,3,2,4]))
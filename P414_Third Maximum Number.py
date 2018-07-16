class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = sorted(list(set(nums)))
        if len(new_nums) < 3:
            return new_nums[-1]
        else:
            return (new_nums[-3])


a = Solution()
print(a.thirdMax([1,2,2,4,5]))